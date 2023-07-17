from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Estado(Base):
    __tablename__ = 'estado'
    cod_uf = Column(Integer, primary_key=True)
    uf = Column(String(2))
    cod_fornecedor = Column(Integer, ForeignKey('fornecedor.cod_fornecedor'))
    nome = Column(String(255))
    fornecedor = relationship("Fornecedor")