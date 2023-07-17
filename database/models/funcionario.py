from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Funcionario(Base):
    __tablename__ = 'funcionario'
    cod_funcionario = Column(Integer, primary_key=True)
    nome = Column(String(255))