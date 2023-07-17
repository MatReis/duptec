from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Pesquisa(Base):
    __tablename__ = 'pesquisa'
    cod_pesquisa = Column(Integer, primary_key=True)
    cod_cliente = Column(Integer)
    cod_uf = Column(Integer, ForeignKey('estado.cod_uf'))
    cod_servico = Column(Integer)
    tipo = Column(Text)
    cpf = Column(String(11))
    cod_uf_nascimento = Column(Integer, ForeignKey('estado.cod_uf'))
    cod_uf_rg = Column(Integer, ForeignKey('estado.cod_uf'))
    data_entrada = Column(DateTime)
    data_conclusao = Column(DateTime)
    nome = Column(String(255))
    nome_corrigido = Column(String(255))
    rg = Column(String(10))
    rg_corrigido = Column(String(10))
    nascimento = Column(DateTime)
    mae = Column(String(255))
    mae_corrigido = Column(String(255))
    anexo = Column(Text)
    estado = relationship("Estado", foreign_keys=[cod_uf])
    estado_nascimento = relationship("Estado", foreign_keys=[cod_uf_nascimento])
    estado_rg = relationship("Estado", foreign_keys=[cod_uf_rg])