from tkinter import *
from datetime import datetime
import pyodbc


######## criando conexao #############

dados_conexao = (
    "Driver={SQLite3 ODBC Driver};"
    "Server=localhost;"
    "Database=Estoque.db;"
    # "unicode_results=True;"
)

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

######## funcionalidades do sistema #############

# print(caixa_texto.get('1.0', END))
# print(nome_insumo.get())
# print(data_insumo.get())
# print(lote_insumo.get())
# print(qtde_insumo.get())

def adicionar_insumo():

    if not nome_insumo.get().strip() or not qtde_insumo.get().strip() or not data_insumo.get() or not lote_insumo.get().strip():
        # exibir uma mensagem -> nome insumo inválido
        # deletar tudo na caixa de texto
        caixa_texto.delete("1.0", END)

        # escrever na caixa de texto
        caixa_texto.insert("1.0", "Nome, Quantidade, Data de validade ou Lote do insumo inválido!")

        # finalizar a função
        return

    # verificando se a data está no formato yyyy-mm-dd
    try:
        datetime.strptime(data_insumo.get(), '%Y-%m-%d') # convertendo a string em data
    except ValueError:
        caixa_texto.delete("1.0", END)
        caixa_texto.insert("1.0", "Data de validades inválida! Use o formato yyyy-mm-dd")
        return

    if len(data_insumo.get()) < 2:
        caixa_texto.delete("1.0", END)

        caixa_texto.insert("1.0", "Data de validade inválida!")

        return

    cursor.execute('''
        INSERT INTO Estoque (Produto, Quantidade, DataValidade, Lote) 
                   VALUES(?, ?, ?, ?)
    ''', (nome_insumo.get(), qtde_insumo.get(), data_insumo.get(), lote_insumo.get()))

    cursor.commit()
    
    # deletar tudo da caixa de texto
    caixa_texto.delete("1.0", END)
    
    # escrever na caixa de texto
    caixa_texto.insert("1.0", f"Insumo {nome_insumo.get()} adicionado com sucesso!")
    
def deletar_insumo():
    if not nome_insumo.get().strip() or not lote_insumo.get().strip():
        # exibir uma mensagem -> nome insumo inválido
        # deletar tudo na caixa de texto
        caixa_texto.delete("1.0", END)

        # escrever na caixa de texto
        caixa_texto.insert("1.0", "Nome ou Lote do insumo inválido!")

        # finalizar a função
        return
    
    # Buscando insumo no DB
    cursor.execute('''
        SELECT * FROM Estoque
                   WHERE Produto = ? AND Lote = ?
    ''', (nome_insumo.get(), lote_insumo.get(), ))

    resultado_busca = cursor.fetchone()

    if resultado_busca is None:

        # limpando a caixa de texto
        caixa_texto.delete("1.0", END)

        # mensagem de retorno que insumo não foi localizado
        caixa_texto.insert("1.0", f"Insumo '{nome_insumo.get()}' pertencente ao Lote '{lote_insumo.get()}' não foi localizado no estoque!")
        return
    
    #  caso encontrar o insumo, deletar o mesmo
    cursor.execute('''
        DELETE FROM Estoque
                   WHERE Produto = ? AND Lote = ?
    ''', (nome_insumo.get(), lote_insumo.get(),))
    cursor.commit()

    # limpar a caixa de texto
    caixa_texto.delete("1.0", END)

    # mensagem de retorno na caixa de texto
    caixa_texto.insert("1.0", f"Insumo {nome_insumo.get()} pertencente ao Lote {lote_insumo.get()} foi deletado com sucesso!")

def consumir_insumo():
    if len(nome_insumo.get()) < 2 or len(lote_insumo.get()) < 1 or len(qtde_insumo.get()) < 1:
        # exibir uma mensagem -> nome insumo inválido
        # deletar tudo na caixa de texto
        caixa_texto.delete("1.0", END)

        # escrever na caixa de texto
        caixa_texto.insert("1.0", "Nome, Lote ou Quantidade do insumo está inválido!")

        # finalizar a função
        return
    
    #  caso encontrar o insumo, consumir o mesmo
    cursor.execute('''
        UPDATE Estoque
                   SET Quantidade = Quantidade - ?
                   WHERE Produto = ? AND Lote = ?
    ''', (qtde_insumo.get(), nome_insumo.get(), lote_insumo.get()))

    cursor.commit()

    # limpar a caixa de texto
    caixa_texto.delete("1.0", END)

    # mensagem de retorno na caixa de texto
    caixa_texto.insert("1.0", f"A quantidade de {qtde_insumo.get()} unidade(s) do insumo {nome_insumo.get()} foi consumido!")


def visualizar_insumo():
    if not nome_insumo.get().strip() or not lote_insumo.get().strip():

        # limpar a caixa de texto
        caixa_texto.delete("1.0", END)

        # escrever mensagem de retorno na caixa de texto
        caixa_texto.insert("1.0", "Nome ou Lote do insumo inválido!")

        # finalizando a função
        return
    

    # pesquisando pelo insumo
    cursor.execute('''
        SELECT * FROM Estoque
                    WHERE Produto = ? and Lote = ?
    ''', (nome_insumo.get(), lote_insumo.get(), ))

    # retornar uma lista com várias tuplas,
    # aonde cada tupla é um registro de insumo
    valores_produto = cursor.fetchall()

    if not valores_produto:
        caixa_texto.delete("1.0", END)
        caixa_texto.insert("1.0", "Produto ou Lote não encontrados no estoque!")
        return

    texto = ""
    for id_produto, nome_produto, qtde_produto, validade_produto, lote_produto in valores_produto:
        texto += f'----- \nProduto: {nome_produto}\nQuantidade: {qtde_produto}\nValidade: {validade_produto}\nLote: {lote_produto}\n-----\n'

    # limpar caixa de texto
    caixa_texto.delete("1.0", END)

    # escrever mensagem de retorno na caixa de texto
    caixa_texto.insert("1.0", texto)
    
    
######### criação da Janela ##################
    
window = Tk()

window.geometry("711x646")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 646,
    width = 711,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"janela/background.png")
background = canvas.create_image(
    355.5, 323.0,
    image=background_img)

img0 = PhotoImage(file = f"janela/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = visualizar_insumo,
    relief = "flat")

b0.place(
    x = 479, y = 195,
    width = 178,
    height = 38)

img1 = PhotoImage(file = f"janela/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = deletar_insumo,
    relief = "flat")

b1.place(
    x = 247, y = 197,
    width = 178,
    height = 36)

img2 = PhotoImage(file = f"janela/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = consumir_insumo,
    relief = "flat")

b2.place(
    x = 479, y = 123,
    width = 178,
    height = 35)

img3 = PhotoImage(file = f"janela/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = adicionar_insumo,
    relief = "flat")

b3.place(
    x = 247, y = 125,
    width = 178,
    height = 34)

entry0_img = PhotoImage(file = f"janela/img_textBox0.png")
entry0_bg = canvas.create_image(
    455.0, 560.0,
    image = entry0_img)

caixa_texto = Text(
    bd = 0,
    bg = "#ffffff",
    fg="#000000",
    highlightthickness = 0)

caixa_texto.place(
    x = 250, y = 502,
    width = 410,
    height = 114)

entry1_img = PhotoImage(file = f"janela/img_textBox1.png")
entry1_bg = canvas.create_image(
    517.0, 294.5,
    image = entry1_img)

nome_insumo = Entry(
    bd = 0,
    bg = "#ffffff",
    fg="#000000",
    highlightthickness = 0)

nome_insumo.place(
    x = 377, y = 278,
    width = 280,
    height = 31)

entry2_img = PhotoImage(file = f"janela/img_textBox2.png")
entry2_bg = canvas.create_image(
    517.0, 340.5,
    image = entry2_img)

data_insumo = Entry(
    bd = 0,
    bg = "#ffffff",
    fg="#000000",
    highlightthickness = 0)

data_insumo.place(
    x = 377, y = 324,
    width = 280,
    height = 31)

entry3_img = PhotoImage(file = f"janela/img_textBox3.png")
entry3_bg = canvas.create_image(
    517.0, 388.5,
    image = entry3_img)

lote_insumo = Entry(
    bd = 0,
    bg = "#ffffff",
    fg="#000000",
    highlightthickness = 0)

lote_insumo.place(
    x = 377, y = 372,
    width = 280,
    height = 31)

entry4_img = PhotoImage(file = f"janela/img_textBox4.png")
entry4_bg = canvas.create_image(
    517.0, 436.5,
    image = entry4_img)

qtde_insumo = Entry(
    bd = 0,
    bg = "#ffffff",
    fg="#000000",
    highlightthickness = 0)

qtde_insumo.place(
    x = 377, y = 420,
    width = 280,
    height = 31)

window.resizable(False, False)
window.mainloop()

cursor.close()
conexao.close()
