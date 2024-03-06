from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Musica(Base):
    __tablename__ = 'musica'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    duracao_ms = Column(Integer, nullable=False)
    artistas = Column(String(255), nullable=False)
    nome_album = Column(String(255))
    data_lancamento = Column(Date, nullable=False)
    total_musicas_album = Column(Integer)
