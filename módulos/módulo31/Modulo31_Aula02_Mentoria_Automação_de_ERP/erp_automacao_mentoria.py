'''
    1. Abrir o ERP (Fakturama)
    2. Clicar no menu New
    3. Clicar em 'New Product'
    4. Preencher os campos
    5. Selecionar imagem
    6. clicar em salvar
'''

import time
import sys
import subprocess
import pyautogui
import pyperclip
import pandas as pd

# CONFIGURAÇÕES INICIAIS
pyautogui.PAUSE = 0.5 # tempo de 1/2s entre cada ação
pyautogui.FAILSAFE = True # configuração para interrompear execução do programa, caso necessário

def log(msg, tipo="info"):
    emoji = {"info": "ℹ️", "success": "✅", "error": "❌", "warn": "⚠️", "wait": "⏳"}.get(tipo, "")
    print(f"{emoji} {msg}")

def find_image(img_path, timeout=20):
    '''  PROCURANDO IMAGEM NA TELA COM TEMPO LIMITE '''
    start_time_process = time.time()
    while time.time() - start_time_process < timeout:
        position = pyautogui.locateOnScreen(img_path, grayscale=True, confidence=0.8)
        if position:
            # log(f"Imagem {img_path} encontrada com sucesso!\n", "success")
            time.sleep(1)
            return position
    print(f"\nTempo excedido!\nA imagem {img_path} não foi encontrada...")
    return None

def find_and_safe_click(img_path, name_item=""):
    ''' CLICA NA ÁREA DA IMAGEM, CASO A MESMA SEJA ENCONTRADA '''
    position_item = find_image(img_path)
    if position_item and name_item:
        log(f"Clicando no(a) Menu/Opção '{name_item}'...\n", "info")
        pyautogui.click(pyautogui.center(position_item))
    elif position_item:
        pyautogui.click(pyautogui.center(position_item))
    else:
        log(f"Erro: Imagem '{img_path} não foi localizada...'", "error")
        sys.exit(1)

def open_application():
    ''' INICIALIZANDO A APLICAÇÃO '''
    subprocess.Popen([r"/Applications/Fakturama2.app/Contents/MacOS/Fakturama"])
    time.sleep(4)

def start_focus_app():
    ''' INICIAR E FOCAR NA JANELA DO FAKTURAMA2 '''
    # descomentar se quiser iniciar o app via script
    # open_application()
    log("Verificando se o Fakturama foi iniciado...\n", "wait")
    find_and_safe_click("assets/logo_fakturama.png")
    log("Aplicação iniciada com sucesso!\n", "success")

    log("Focando na janela da aplicação...\n", "info")
    header_position = find_image("assets/corner_screen_fakturama.png")
    if header_position:
        pyautogui.click(pyautogui.center(header_position))
    else:
        print("Cabeçalho da aplicação nao lozalizado...")
        sys.exit(1)

def click_onright_image(img_position):
    ''' CALCULANDO A POSIÇÃO DE CLIQUE À DIREITA DA IMAGEM '''
    return img_position[0] + img_position[2], img_position[1] + img_position[3] // 2

def write_text(text):
    pyperclip.copy(text)
    pyautogui.hotkey("command", "v")

def find_field_and_enter_information(img_path, text):
    ''' PREENCHER CAMPOS DO FORM, ENCONTRANDO E CLICANDO À DIREITA DA IMAGEM '''
    position_item = find_image(img_path)
    if position_item:
        pyautogui.click(click_onright_image(position_item))
        write_text(text)
        # pyautogui.write(text)
    else:
        print(f"Erro: Campo '{img_path}' não foi localizado...")
        sys.exit(1)

def verify_extension():
    jpg_selected = find_image("assets/select_jpg_extension.png", timeout=5)

    if jpg_selected:
        log("Extensão JPG já está selecionada! Continuando...\n", "info")
    else:
        # se a extensão JPG não foi selecionada, tentar encontrar o formato PNG e alterar
        find_and_safe_click("assets/select_png_extension.png")
        find_and_safe_click("assets/select_jpg_extension.png")

# programa principal
if __name__ == "__main__":
    # abrindo o sistema ERP (fakturama)
    # open_application()
    # time.sleep(4)

    ''' confirmando que o software abriu com sucesso '''
    find_image('assets/logo_fakturama.png')

    ''' dando foco na aplicação '''
    start_focus_app()

    ''' Lógica para adicionar vários produtos '''

    tabela_produtos = pd.read_excel("Produtos.xlsx")
    for linha in tabela_produtos.index:
        id = tabela_produtos.loc[linha, "ID"]
        name = tabela_produtos.loc[linha, "Nome"]
        category = tabela_produtos.loc[linha, "Categoria"]
        gtin = tabela_produtos.loc[linha, "GTIN"]
        supplier = tabela_produtos.loc[linha, "Supplier"]
        description = tabela_produtos.loc[linha, "Descrição"]
        image = tabela_produtos.loc[linha, "Imagem"]
        price = tabela_produtos.loc[linha, "Preço"]
        cost = tabela_produtos.loc[linha, "Custo"]
        stock = tabela_produtos.loc[linha, "Estoque"]

        ''' Formatando o preço, custo e estoque '''
        price_formatted = f"{price:.2f}".replace(".", ",")
        cost_formatted = f"{cost:.2f}".replace(".", ",")
        stock_formatted = f"{stock:.2f}".replace(".", ",")

        find_and_safe_click("assets/menu_new.png", "New")
        find_and_safe_click("assets/menu_new_product.png", "New Product")
        find_field_and_enter_information("assets/item_number.png", str(id))
        find_field_and_enter_information("assets/name_product.png", str(name))
        find_field_and_enter_information("assets/category_product.png", str(category))
        find_field_and_enter_information("assets/GTIN_product.png", str(gtin))
        find_field_and_enter_information("assets/supplier_code_product.png", str(supplier))
        find_field_and_enter_information("assets/description_product.png", str(description))
        find_field_and_enter_information("assets/price_product.png", str(price_formatted))
        find_field_and_enter_information("assets/cost_price_product.png", str(cost_formatted))
        find_field_and_enter_information("assets/stock_product.png", str(stock_formatted))
        find_and_safe_click("assets/select_picture.png", "Select Picture")
        
        ''' verificando no finder extensao da picture '''
        verify_extension()
        time.sleep(0.5)
        
        ''' realizando a busca e seleção da picture no finder '''
        pyautogui.hotkey("command", "shift", "g")
        pyautogui.write("~")
        pyautogui.press("space")
        pyautogui.write(rf"/Documents/AssetsProjectERPFakturama/{str(image)}")
        time.sleep(1)
        pyautogui.press("return")
        time.sleep(1)
        pyautogui.press("return")
        time.sleep(0.5)

        ''' salvando picture '''
        find_and_safe_click("assets/button_save.png", "Salvar..")
        time.sleep(0.5)
        find_and_safe_click("assets/close_window.png")
        time.sleep(0.5)
