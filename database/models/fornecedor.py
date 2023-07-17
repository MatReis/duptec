from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Fornecedor(Base):
    __tablename__ = 'fornecedor'
    cod_fornecedor = Column(Integer, primary_key=True)
    nome = Column(String(255))