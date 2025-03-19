# crud.py - FUNÇÕES DE CRIAÇÃO, LEITURA, ATUALIZAÇÃO E EXCLUSÃO

import os

from database import SessionLocal
from models import Usuario, Livro
from sqlalchemy.exc import SQLAlchemyError
from utils import gerar_senha_hash

colors = (
    '\033[m', # 0 - SEM COR
    '\033[0;31m', # 1 - VERMELHO
    '\033[0;32m', # 2 - VERDE
    '\033[0;33m', # 3 - AMARELO
    '\033[0;34m', # 4 - AZUL
    '\033[0;35m', # 5 - ROXO
    '\033[0;36m', # 6 - BRANCO
)

def jump_line(n):
    print('\n'*n)

def print_line_separator(cor=0):
    width_terminal = os.get_terminal_size().columns
    print(colors[cor], end='')
    print('-'*width_terminal)
    print(colors[0], end='')


def print_message_centralized(msg, cor=0):
    width_terminal = os.get_terminal_size().columns
    space = (width_terminal - len(msg)) // 2

    message = ' ' * space + msg + ' '

    print(colors[cor], end='')
    print(message)
    print(colors[0], end='')

def criar_usuario(nome, email, senha):
    senha_hash = gerar_senha_hash(senha)
    with SessionLocal() as session:
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha_hash)
            session.add(usuario)
            session.commit()
            jump_line(1)
            print_line_separator(2)
            print_message_centralized('✅  Usuário criado com sucesso!', 2)
            print_line_separator(2)
        except SQLAlchemyError as e:
            session.rollback()
            print_line_separator(1)
            print_message_centralized(f'❌ Erro ao criar usuário: {e}',1)
            print_line_separator(1)

def listar_usuarios():
    with SessionLocal() as session:
        return session.query(Usuario).all()
    
def buscar_usuario_por_email(email):
    with SessionLocal() as session:
        return session.query(Usuario).filter_by(email=email).first()
    
def cadastrar_livro(titulo, qtde_paginas, email_usuario_leitor):
    with SessionLocal() as session:
        usuario_leitor = session.query(Usuario).filter_by(email=email_usuario_leitor).first()
        if usuario_leitor:
            livro = Livro(titulo=titulo, qtde_paginas=qtde_paginas, usuario_leitor=usuario_leitor.id)
            session.add(livro)
            session.commit()
            jump_line(1)
            print_line_separator(2)
            print_message_centralized('📚  Livro cadastrado com sucesso!', 2)
            print_line_separator(2)
        else:
            print_line_separator(1)
            print_message_centralized('❌  Usuário não encontrado no sistema!', 1)
            print_line_separator(1)

def listar_livros():
    with SessionLocal() as session:
        return session.query(Livro).all()

def buscar_livro_por_titulo(titulo):
    with SessionLocal() as session:
        return session.query(Livro).filter_by(titulo=titulo).first()

def atualizar_nome_usuario(email, novo_nome):
    with SessionLocal() as session:
        usuario = session.query(Usuario).filter_by(email=email).first()
        if usuario:
            usuario.nome = novo_nome
            session.commit()
            jump_line(1)
            print_line_separator(2)
            print_message_centralized('✅  Nome atualizado no sistema com sucesso!', 2)
            print_line_separator(2)
        else:
            print_line_separator(1)
            print_message_centralized('❌  Usuário não encontrado no sistema!', 1)
            print_line_separator(1)


def deletar_usuario(email):
    with SessionLocal() as session:
        usuario = session.query(Usuario).filter_by(email=email).first()
        if usuario:
            session.delete(usuario)
            session.commit()
            jump_line(1)
            print_line_separator(2)
            print_message_centralized('❌  Usuário deletado do sistema com sucesso!', 2)
            print_line_separator(2)
        else:
            print_line_separator(1)
            print_message_centralized('Usuário não encontrado!', 1)
            print_line_separator(1)
