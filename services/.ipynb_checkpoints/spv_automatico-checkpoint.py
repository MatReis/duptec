import datetime
import time
import sys
import os
from database.connection import Connection
from database.models.estado import Estado
from database.models.lote import Lote
from database.models.lote_pesquisa import LotePesquisa
from database.models.pesquisa import Pesquisa
from database.models.pesquisa_spv import PesquisaSPV
from database.models.servico import Servico
from sqlalchemy import distinct, func
from provider.site_strategy import Site
from provider.sites.tjsp import TJSP



class SPVAutomatico():

    def __init__(self, filtro='') -> None:
        self.filtro = filtro

    # adiciona paginação
    def conectaBD(filtro, pagina=1, total_pagina=30):
        inicio = (pagina - 1) * total_pagina
        final = pagina * total_pagina

        conexao = Connection()
        session = conexao.get_session()

        try:    
            query = session.query(
                distinct(Pesquisa.cod_cliente),
                Pesquisa.cod_pesquisa, 
                Estado.uf, 
                Pesquisa.data_entrada,
                func.coalesce(Pesquisa.nome_corrigido, Pesquisa.nome).label('Nome'), 
                Pesquisa.cpf,
                func.coalesce(Pesquisa.rg_corrigido, Pesquisa.rg).label('RG'), 
                Pesquisa.nascimento,
                func.coalesce(Pesquisa.mae_corrigido, Pesquisa.mae).label('Mae'),
                Pesquisa.anexo.label('Anexo'),
                PesquisaSPV.Resultado, 
                PesquisaSPV.cod_spv_tipo)\
                .join(Servico, Pesquisa.cod_Servico == Servico.cod_servico)\
                .outerjoin(LotePesquisa, Pesquisa.cod_pesquisa == LotePesquisa.cod_pesquisa)\
                .outerjoin(Lote, Lote.cod_lote == LotePesquisa.cod_lote)\
                .outerjoin(Estado, Estado.cod_uf == Pesquisa.cod_uf)\
                .outerjoin(PesquisaSPV, (PesquisaSPV.cod_pesquisa == Pesquisa.cod_pesquisa) &
                            (PesquisaSPV.cod_spv == 1) & (PesquisaSPV.filtro == filtro))\
                .filter(Pesquisa.data_conclusao.is_(None))\
                .filter(PesquisaSPV.resultado.is_(None))\
                .filter(Pesquisa.tipo == 0)\
                .filter(Pesquisa.cpf != '')\
                .filter((Estado.uf == 'SP') | (Pesquisa.cod_uf_nascimento == 26) |
                        (Pesquisa.cod_uf_rg == 26))\
                .group_by(Pesquisa.cod_pesquisa)\
                .order_by(func.lower(Pesquisa.nome).asc(), PesquisaSPV.resultado.desc())\
                .slice(inicio, final)
            
            if filtro in (1, 3):
                query = query.filter(Pesquisa.RG != '')

            resultado = query.all()

            return resultado
        finally:
            session.close()

    def pesquisa(self):
        w = 0
        tempo_inicio = datetime.datetime.now()

        i = self.filtro
        qry = self.conectaBD(self.filtro)

        if (len(qry) > 0):
            for dados in qry:
                codCliente, codPesquisa, uf, dataEntrada, nome, cpf, rg, dataNascimento, nomeMae, anexo, resultado, spvTipo = dados
                
                self.executaPesquisa(self, self.filtro, nome, cpf, rg, codPesquisa, spvTipo)
                tempo_fim = datetime.datetime.now()
                tempo_gasto = round((tempo_fim - tempo_inicio).total_seconds(), 2)
                if (tempo_gasto >= 600):
                    break
    
            tempo_gasto = 0
            i = i + 1
            if (i <= 3):
                print('RECOMENÇANDO COM O FILTRO '+ str(i))
                p = SPVAutomatico(i)
                p.pesquisa()
            else:
                print('RECOMEÇANDO')
                self.restarta_programa(self)
        else:
            # TENTA COM O PRÓXIMO FILTRO
            w = w + 1
            print('AGUARDANDO PARA RECOMEÇAR')
            time.sleep(60)
            if (w >= 20):
                time.sleep(3600)
                self.restarta_programa(self)
            else:
                self.restarta_programa(self)

    @staticmethod
    def executaPesquisa(self, filtro, nome, cpf, rg, codPesquisa):
        conection = Connection()  
        session = conection.get_session()
        if (filtro == 0 and cpf != None):
            aux = cpf
        elif (filtro == 3 or (filtro == 1 and rg != None and rg != '')):
            aux = rg
        elif (filtro == 2 and nome != None and nome != ''):
            aux = nome
        else:
            return
        
        site = self.carregaSite(self, filtro, aux)
        result = self.checaResultado(site, codPesquisa)
        
        dict_pesquisa = {
            "cod_pesquisa": codPesquisa,
            "cod_spv": 1,
            "cod_spv_computador": 36,
            "resultado": result,
            "cod_funcionario": -1,
            "filtro": filtro,
            "website_id": 1,
        }

        pesquisa = PesquisaSPV(**dict_pesquisa)

        try:
            session.add(pesquisa)

            session.commit()

        finally:
            session.close()

    @staticmethod
    def checaResultado(site, codPesquisa):
        exec(open('.env').read())
        final_result = 7
        if (os.getenv('NADA_CONSTA') in site):
            final_result = 1
        elif ((os.getenv('CONSTA01') in site) \
              or (os.getenv('CONSTA02') in site)) and \
                ('Criminal' in site) or ('criminal' in site):
            final_result = 2
        elif ((os.getenv('CONSTA01') in site) or (os.getenv('CONSTA02') in site)):
            final_result = 5

        return final_result
    
    @staticmethod
    def carregaSite(self, filtro, documento):

        site = Site(filtro, documento)

        try: 
            site.consultar(TJSP())
        except:
            time.sleep(120)
            self.restarta_programa(self)

        browser = site.dados()

        return browser.page_source

    @staticmethod
    def restarta_programa(self):
        try:
            python = sys.executable
            os.execl(python, python, * sys.argv)
        except:
            print('PROGRAMA ENCERRADO')
            quit()