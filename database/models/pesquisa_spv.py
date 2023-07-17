from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class PesquisaSPV(Base):
    __tablename__ = 'pesquisa_spv'
    cod_pesquisa = Column(Integer, primary_key=True)
    cod_spv = Column(Integer)
    cod_spv_computador = Column(Integer)
    cod_spv_tipo = Column(Integer)
    cod_funcionario = Column(Integer, ForeignKey('funcionario.cod_funcionario'))
    filtro = Column(Integer)
    website_id = Column(Integer)
    resultado = Column(String(255))
    funcionario = relationship("Funcionario")