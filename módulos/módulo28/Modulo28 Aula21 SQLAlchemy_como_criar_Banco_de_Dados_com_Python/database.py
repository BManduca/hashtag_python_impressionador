# CONEXÃO COM O BANCO

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///banco/db_biblioteca.db'

# echo=True => exibir no console todas as consultas SQL que ele está executando.
engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine)
