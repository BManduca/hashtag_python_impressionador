# CÓDIGO PRINCIPAL (CHAMADA DE FUNÇÕES)

import os
import time
import sys
from database import engine
from models import Base
from crud import (
    buscar_livro_por_titulo,
    criar_usuario,
    deletar_usuario,
    listar_livros,
    listar_usuarios,
    buscar_usuario_por_email,
    cadastrar_livro,
    atualizar_nome_usuario,
    print_line_separator,
    print_message_centralized
)

def jump_line(n):
    print('\n'*n)

def limpar_tela():
    # FUNÇÃO DESTINADA A LIMPAR A TELA NOS SISTEMAS WINDOWS E LINUX/MAC
    time.sleep(6)
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    print_line_separator(2)
    print_message_centralized('Menu', 2)
    print_line_separator(2)
    print_message_centralized('1 => Criar usuário', 2)
    print_message_centralized('2 => Listar usuários', 2)
    print_message_centralized('3 => Buscar usuário por e-mail', 2)
    print_message_centralized('4 => Cadastrar livro para um usuário', 2)
    print_message_centralized('5 => Listar livros', 2)
    print_message_centralized('6 => Buscar livro por título', 2)
    print_message_centralized('7 => Atualizar nome de um usuário', 2)
    print_message_centralized('8 => Deletar usuário', 2)
    print_message_centralized('9 => Encerrar programa', 2)
    print_line_separator(2)


def main():
    # criando as tabelas no banco de dados (caso não existam)
    Base.metadata.create_all(bind=engine)

    while True:
        exibir_menu()
        jump_line(1)
        opc = input('Escolha uma opção: ')
        jump_line(1)

        if opc == '1':
            nome = input('Insira nome do usuário: ')
            email = input('Insira o e-mail do usuário: ')
            senha = input('Senha do usuário: ')
            jump_line(1)
            criar_usuario(nome, email, senha)

        elif opc == '2':
            usuarios = listar_usuarios()
            if usuarios:
                jump_line(1)
                print_line_separator(4)
                for usuario in usuarios:
                    print_message_centralized(f'ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}, Ativo: {usuario.ativo}', 4)
                print_line_separator(4)
            else:
                jump_line(1)
                print_line_separator(3)
                print_message_centralized('⚠️  Nenhum usuário cadastrado no sistema.', 3)
                print_line_separator(3)

        elif opc == '3':
            email = input('Informe o e-mail do usuário: ')
            usuario = buscar_usuario_por_email(email)

            if usuario:
                jump_line(1)
                print_line_separator(2)
                print_message_centralized('📋 Informações usuário:')
                print_message_centralized(f'🔎 Usuário: {usuario.nome}, E-mail: {usuario.email}, Ativo: {usuario.ativo}', 2)
                print_line_separator(2)
            else:
                jump_line(1)
                print_line_separator(1)
                print_message_centralized('❌  Usuário não encontrado no sistema!', 1)
                print_line_separator(1)

        elif opc == '4':
            email_usuario_leitor = input('Informe e-mail do usuário responsável pelo livro: ')
            titulo = input('Informe o título do livro: ')
            qtde_paginas = input('Informa a quantidade de páginas: ')

            if qtde_paginas.isdigit():
                cadastrar_livro(titulo, int(qtde_paginas), email_usuario_leitor)
            else:
                jump_line(1)
                print_line_separator(3)
                print_message_centralized('⚠️  Erro: A quantidade de páginas do livro deve ser um número!', 3)
                print_line_separator(3)

        elif opc == '5':
            livros = listar_livros()

            if livros:
                jump_line(1)
                print_line_separator(4)
                for livro in livros:
                    print_message_centralized(f'ID: {livro.id}, Título: {livro.titulo}, Quantidade de Páginas: {livro.qtde_paginas}, Usuário leitor: {livro.usuario_leitor}', 4)
                print_line_separator(4)
            else:
                jump_line(1)
                print_line_separator(3)
                print_message_centralized('⚠️  Nenhum livro cadastrado no sistema.', 3)
                print_line_separator(3)

        elif opc == '6':
            titulo = input('Informe o título do livro: ')
            livro = buscar_livro_por_titulo(titulo)

            if titulo:
                jump_line(1)
                print_line_separator(2)
                print_message_centralized('📚 Informações livro:')
                print_message_centralized(f'🔎 Título: {livro.titulo}, Quantidade de páginas: {livro.qtde_paginas}, Usuário leitor: {livro.usuario_leitor}', 2)
                print_line_separator(2)
            else:
                jump_line(1)
                print_line_separator(1)
                print_message_centralized('❌ Livro não encontrado no sistema!', 1)
                print_line_separator(1)

        elif opc == '7':
            email = input('Insira o e-mail do usuário que deseja atualizar: ')
            novo_nome = input('Insira o nome atualizado do usuário: ')
            atualizar_nome_usuario(email, novo_nome)

        elif opc == '8':
            email = input('Insira o e-mail do usuário que deseja deletar: ')
            deletar_usuario(email)

        elif opc == '9':
            print_line_separator(4)
            print_message_centralized('👋  Finalizando programa..', 4)
            print_line_separator(4)
            break

        else:
            print_line_separator(3)
            print_message_centralized('⚠️  Opção inválida! Tente novamente!', 3)
            print_line_separator(3)

        limpar_tela() # chamando função para limpar a tela, antes de aparecer o menu

if __name__ == "__main__":
    main()
