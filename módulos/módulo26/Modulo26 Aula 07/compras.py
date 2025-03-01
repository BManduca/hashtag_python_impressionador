from datetime import datetime
from pathlib import Path
import os
import json
import time

# obtendo a data atual
data_atual = datetime.now()

dia, mes, ano = data_atual.day, data_atual.month, data_atual.year

Path("listas_compras_mensais/").mkdir(parents=True, exist_ok=True)
caminho_listas_compras = Path("listas_compras_mensais/")


def message_centralized(msg, wid, color):
    colors = {
        "vermelho": "\033[91m",
        "verde": "\033[92m",
        "amarelo": "\033[93m",
        "azul": "\033[94m",
        "magenta": "\033[95m",
        "ciano": "\033[96m",
        "branco": "\033[97m",
        "reset": "\033[0m",
    }

    tam = len(msg)
    space = (wid - tam) // 2
    msg_final = " " * space + msg + " " * space

    # se o texto não puder ser centralizado perfeitamente, ajustar o mesmo uma posição para a direita
    if len(msg_final) < wid:
        msg_final += " "

    select_color = colors.get(color.lower(), colors["reset"])
    print(f"{select_color}{msg_final}{colors['reset']}")


def adicionar_item(compras, nome_item, quantidade):
    compras[nome_item] = quantidade


def remover_item(compras, nome_item):
    if compras == {}:
        print("A lista está vazia!")
    elif nome_item in compras:
        del compras[nome_item]
        time.sleep(2)
        return
    else:
        # print(f'Item {nome_item} não presente na lista!')
        message_centralized(
            f"Item {nome_item} não está presente na lista!", 60, "vermelho"
        )


def visualizar_compras(compras):
    print()
    for item, quantity in compras.items():
        print(f"{item}: {quantity}")
    print()
    print("\nPressione enter para continuar...")
    input()


def salvar_compras(compras, nome_arquivo):
    arquivo_compras_data = f"{nome_arquivo}_{dia}_{mes}_{ano}"

    # conferencia para verificar se o nome do arquivo termina com .json
    if not arquivo_compras_data.endswith(".json"):
        arquivo_compras_data += ".json"

    caminho_arquivo_compras = (
        caminho_listas_compras / arquivo_compras_data
    )
    with open(caminho_arquivo_compras, "w", encoding="utf-8") as arquivo:
        # dump -> "jogar" as informações presentes no dicionario compras
        # para dentro do arquivo compras.json
        json.dump(compras, arquivo, ensure_ascii=False)


def visualizar_listas_compras(caminho_listas):
    os.system("cls" if os.name == "nt" else "clear")
    print("\n\nListas de compras disponíveis:")

    # Convertendo iterador em lista
    arquivos_json_lista_compras = list(caminho_listas.iterdir())

    if not arquivos_json_lista_compras:
        print("Nenhuma lista encontrada!")
        time.sleep(2)
        return
    
    for i, arquivo in enumerate(arquivos_json_lista_compras):
        print(f"{i + 1} - {arquivo.name}")

    try:
        escolha = int(input("\nEscolha uma lista para carregar (0 para cancelar): "))
    except ValueError:
        print("Opção inválida")
        time.sleep(2)
        return

    if escolha == 0:
        return
    if escolha < 0 or escolha > len(arquivos_json_lista_compras):
        print("Opção inválida")
        time.sleep(2)
        return

    arquivo_selecionado = arquivos_json_lista_compras[escolha - 1]
    compras = carregar_compras(arquivo_selecionado)
    gerenciar_compras(compras, arquivo_selecionado)

    # maneira alternativa - Professor

    # arquivos = [arquivo for arquivo in os.listdir("listas_compras_mensais")]
    #     if not arquivos:
    #         print("Nenhuma lista encontrada.")
    #         time.sleep(3)
    #         continue


def carregar_compras(nome_arquivo):
    with open(str(nome_arquivo), "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def gerenciar_compras(compras, nome_arquivo=None):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("1 Adicionar item")
        print("2 Remover item")
        print("3 Visualizar lista")
        print("4 Salvar e sair")
        print("5 Sair sem salvar")
        escolha = input("\n\nEscolha uma opção: ")

        if escolha == "1":
            os.system("cls" if os.name == "nt" else "clear")
            item = input("\nDigite o nome do item: ")
            quantidade = float(input("\nDigite a quantidade: "))
            adicionar_item(compras, item, quantidade)
        elif escolha == "2":
            nome_item = input("Digite o nome do item a ser removido: ")
            remover_item(compras, nome_item)
        elif escolha == "3":
            visualizar_compras(compras)
        elif escolha == "4":
            if nome_arquivo is None:
                nome_arquivo = input("Digite o nome do arquivo para salvar: ")
            # conferencia para verificar se o nome do arquivo termina com .json
            # if not nome_arquivo.endswith(".json"):
            #     nome_arquivo += ".json"
            salvar_compras(compras, nome_arquivo)
            break
        elif escolha == "5":
            break
        else:
            print("Opção inválida")
            time.sleep(2)


def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("1 Criar uma nova lista de compras")
        print("2 Carregar uma lista existente")
        print("3 Sair")
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            compras = {}
            gerenciar_compras(compras)
        elif escolha == "2":
            visualizar_listas_compras(caminho_listas_compras)

        elif escolha == "3":
            break
        else:
            print("Opção inválida")
            time.sleep(2)


if __name__ == "__main__":
    main()
