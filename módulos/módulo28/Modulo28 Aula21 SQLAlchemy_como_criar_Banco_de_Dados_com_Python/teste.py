import os

colors = (
    '\033[m', # 0 - SEM COR
    '\033[0;31m', # 1 - VERMELHO
    '\033[0;32m', # 2 - VERDE
    '\033[0;33m', # 3 - AMARELO
    '\033[0;34m', # 4 - AZUL
    '\033[0;35m', # 5 - ROXO
    '\033[0;36m', # 6 - BRANCO
)

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


print_line_separator(2)
print_message_centralized('Este é um teste', 2)
print_line_separator(2)
