from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class LotePesquisa(Base):
    __tablename__ = 'lote_pesquisa'
    cod_lote_pesquisa = Column(Integer, primary_key=True)
    cod_lote = Column(Integer, ForeignKey('lote.cod_lote'))
    cod_pesquisa = Column(Integer, ForeignKey('pesquisa.cod_pesquisa'))
    cod_funcionario = Column(Integer, ForeignKey('funcionario.cod_funcionario'))
    cod_funcionario_conclusao = Column(Integer, ForeignKey('funcionario.cod_funcionario'))
    cod_fornecedor = Column(Integer, ForeignKey('fornecedor.cod_fornecedor'))
    data_entrada = Column(DateTime)
    data_conclusao = Column(DateTime)
    cod_uf = Column(Integer, ForeignKey('estado.cod_uf'))
    obs = Column(Text)
    lote = relationship("Lote")
    funcionario = relationship("Funcionario", foreign_keys=[cod_funcionario])
    funcionario_conclusao = relationship("Funcionario", foreign_keys=[cod_funcionario_conclusao])
    fornecedor = relationship("Fornecedor")
    estado = relationship("Estado")