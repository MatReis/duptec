from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Lote(Base):
    __tablename__ = 'lote'
    cod_lote = Column(Integer, primary_key=True)
    cod_lote_prazo = Column(Integer)
    data_criacao = Column(DateTime)
    cod_funcionario = Column(Integer, ForeignKey('funcionario.cod_funcionario'))
    tipo = Column(String(255))
    prioridade = Column(String(255))
    funcionario = relationship("Funcionario")