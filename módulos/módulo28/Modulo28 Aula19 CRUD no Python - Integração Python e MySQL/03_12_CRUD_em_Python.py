from email import message
import os
import time
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def message_centralized(msg, wid):
    tam = len(msg)
    space = (wid - tam) // 2
    text = ' ' * space + msg + ' ' * space
    # Se o texto não puder ser centralizado perfeitamente, ajuste uma posição para a direita
    if len(text) < wid:
        text += ' '
    return text

try:
    conexao = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_USER_PASSWORD'),
        database=os.getenv('DB_NAME'),
    )

    print('Conexão efetuada com sucesso!\n\n')

    # cursor -> executar os comandos da conexao
    cursor = conexao.cursor()

    # CRUD

    # CREATE
    # nome_produto = "todynho"
    # valor = 5
    # comando = 'INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)'
    # valores = (nome_produto, valor)
    # cursor.execute(comando, valores)
    # conexao.commit() # edita o banco de dados
    # print('\n-------------------------------------------------------------')
    # print(message_centralized(f'O produto {nome_produto} foi registrado com sucesso!', 60))
    # print('-------------------------------------------------------------\n\n')


    # READ
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall() # ler o banco de dados
    print('--------------------------------------------------')
    print(message_centralized('Lista de produtos', 50))
    print('--------------------------------------------------')
    for id, produto, vlr_produto in resultado:
        print(f'{id} -> Produto: {produto} | Valor: R$ {vlr_produto:.2f}')
    print('--------------------------------------------------')
    

    # UPDATE
    # nome_produto = "chocolate"
    # valor = 13
    # #maneira mais seguras de passar variáveis para o SQL é através de placeholders
    # comando = 'UPDATE vendas SET valor = %s WHERE nome_produto = %s'
    # dados = (valor, nome_produto)
    # cursor.execute(comando, dados)

    # conexao.commit() # edita o banco de dados
    # print(f'\n-------------------------------------------------------\n\nO valor do produto {nome_produto} foi atualizado com sucesso!\n\n-------------------------------------------------------\n\n')

    # DELETE
    # nome_produto = "bolacha maizena"
    # comando = 'DELETE FROM vendas WHERE nome_produto = %s'
    # dados = (nome_produto, )
    # cursor.execute(comando, dados)

    # conexao.commit() # edita o banco de dados
    # print('\n-------------------------------------------------------------')
    # print(message_centralized(f'O produto {nome_produto} foi deletado com sucesso!', 60))
    # print('-------------------------------------------------------------\n\n')

except mysql.connector.Error as erro:
    print(f'''
          ------------------------------------------------\n
          Erro ao conectar ou executar o banco de dados: {erro}
          \n------------------------------------------------\n\n
        ''')

finally:
    if cursor:
        cursor.close()

    if conexao:
        conexao.close()
        print('\n--------------------------------')
        print(message_centralized('Encerrando conexão...', 36))
        print('--------------------------------\n')
        for i in range (3, 0, -1):
            print(message_centralized(str(i), 30))
            print()
            time.sleep(2)
        print('\n--------------------------------')
        print(message_centralized('Conexão encerrada!', 32))
        print('--------------------------------\n')
