# pylint: disable=invalid-name
# operações

'''
----------------------------------------------------------------

  Colors em python, este código se inicia com \033[

  0 => none (sem estilo)
  1 => bold(negrito)
  2 => Fraco
  3 => itálico
  4 => underline (sublinhado)
  7 => negative (inverter as configurações Fundo vai pra letra e letra fundo)

  ----------------------------------------------------------------
  Cores para o texto:
  30 => Branco
  31 => Vermelho
  32 => Verde
  33 => Amarelo
  34 => Azul
  35 => Magenta
  36 => Ciano
  37 => Cinza

  ----------------------------------------------------------------
  Cores para o fundo:
  40 = Branco
  41 = Vermelho
  42 = Verde
  43 = Amarelo
  44 = Azul
  45 = Magenta
  46 = Ciano
  47 = Cinza

  ----------------------------------------------------------------

'''

import os

colors=('\033[m',      # 0 - sem cores
        '\033[0;31m',  # 1 - vermelho
        '\033[0;32m',  # 2 - verde
        '\033[0;33m',  # 3 - amarelo
        '\033[0;34m',  # 4 - azul
        '\033[0;35m',  # 5 - roxo
        '\033[7;30m'   # 6 - branco
        )

# imprimindo linha em tamanho especifico
def print_line_separator(cor=0):
    width_terminal = os.get_terminal_size().columns
    print(colors[cor], end='')
    print('-'*width_terminal)
    print(colors[0], end='')


# centralizando a mensagem
def message_centralized(msg, wid: int):
    tam = len(msg)
    space = (wid - tam) // 2
    text = ' ' * space + msg + ' ' * space

    # se o texto não puder ser centralizado perfeitamente, ajuste a posição para a direita

    if len(text) < wid:
        text += ''

    return text

# imprimindo a mensagem centralizada
def print_text_centralized(msg, cor=0):
    width_terminal = os.get_terminal_size().columns
    space = (width_terminal - len(msg)) // 2
    # message = message_centralized(msg, wid)
    message = ' ' * space + msg + ' '
    print(colors[cor], end='')
    print(message)
    print(colors[0], end='')

def jump_line(n):
    print('\n'*n)

def centralized_input(msginput):
    #obtendo o tamanho da janela do terminal
    width_terminal = os.get_terminal_size().columns

    # calcular quantos espaços adicionar antes da mensagem para centralizar
    space = (width_terminal - len(msginput)) // 2

    # Exibindo a mensagem centralizada e realizar a captura do input realizada pelo user
    return input(' ' * space + msginput)

sum_numbers = 1 + 1
mult = 4 * 2
exp = 2 ** 3
divisao = 14 / 7
resto = 7 % 3

print(f'Soma 1 + 1 = {sum_numbers}')
print(f'Multiplicação de 4 por 2 = {mult}')
print(f'2 elevado na 3 = {exp}')
print(f'Divisão de 14 por 7 = {divisao}')
print(f'Resto da divisão de 7 por 3 = {resto}')

jump_line(4)
print_line_separator()
jump_line(1)
print_text_centralized('Aula sobre varíaveis..', 4)

qtd_vendas = 1500

print_text_centralized(f'Quantidade de vendas = {qtd_vendas}', 4)
jump_line(1)

print_line_separator()
jump_line(1)

print_text_centralized('Aula sobre Inputs', 4)

jump_line(2)

name = centralized_input('Insira o seu nome: ')
jump_line(1)
print_text_centralized(f' ==> Seja bem-vindo {name} <== ', 2)
jump_line(1)

print_line_separator()
