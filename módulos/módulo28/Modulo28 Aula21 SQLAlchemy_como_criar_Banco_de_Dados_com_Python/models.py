# MODELOS DAS TABELAS

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True) # evitar duplicidade
    senha = Column(String, nullable=False)
    ativo = Column(Boolean, default=True)

    # relação entre o modelo Usuario e o modelo Livro, dizendo que um usuário pode possuir vários livros (1:N)
    livros = relationship("Livro", back_populates="usuario")

class Livro(Base):
    __tablename__ = 'livros'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    qtde_paginas = Column(Integer, nullable=False)
    usuario_leitor = Column(Integer, ForeignKey("usuarios.id"))

    # definindo a outra ponta da relação, indicando que cada livro pertence a um usuário (N:1), pois, vários livros
    # podem pertencer a um mesmo usuário
    usuario = relationship("Usuario", back_populates="livros")
