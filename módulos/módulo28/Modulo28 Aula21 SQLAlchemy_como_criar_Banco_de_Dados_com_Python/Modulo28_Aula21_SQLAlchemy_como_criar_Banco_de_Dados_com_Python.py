from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///banco/meubanco.db")
# criando objeto da sessão
Session = sessionmaker(bind=db)
# criando/inicializando sessão
session = Session()

Base = declarative_base()

# as tabelas
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    # método construtor da classe usuário
    def __init__(self, nome, email, senha, ativo=True):
        # self -> referência ao próprio objeto(instância) que está sendo criado.
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo


# Livros
class Livro(Base):
    __tablename__ = "livros"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qtde_paginas = Column("qtde_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id"))

    # método construtor da classe livro
    def __init__(self, titulo, qtde_paginas, dono):
        # self -> referência ao próprio objeto(instância) que está sendo criado.
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono


Base.metadata.create_all(bind=db)

# CRUD

# C - Create User
# usuario = Usuario(nome="Brunno", email="brunno@email.com", senha="algo@1234")
# session.add(usuario)
# session.commit()

# R - READ
# lista_usuarios = session.query(Usuario).all() # listagem completa
# print(lista_usuarios)
usuario_lira2 = session.query(Usuario).filter_by(email="qlqcoisa2@email.com").first()
usuario_brunno = session.query(Usuario).filter_by(email="brunno@email.com").first()
# print(usuario_lira2)
# print(usuario_lira2.nome)
# print(usuario_lira2.email)
# print(usuario_lira2.ativo)

# C - Create Livro 
# livro = Livro(titulo="Nome do Vento", qtde_paginas=1000, dono=usuario_brunno.id)
# session.add(livro)
# session.commit()

# U - Update
# usuario_brunno.nome = "Brunno Manduca"
# session.add(usuario_brunno)
# session.commit()

# D - Delete
session.delete(usuario_lira2)
session.commit()
