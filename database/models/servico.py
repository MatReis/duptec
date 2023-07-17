from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Servico(Base):
    __tablename__ = 'servico'
    cod_servico = Column(Integer, primary_key=True)
    civel = Column(String(255))
    criminal = Column(String(255))
