import os
import wind32com.client as win32

outlook = wind32.Dispatch("outlook.application")

email = outlook.CreateItem(0)

# outlook.Session.Accounts -> lista com todas as contas vinculadas no outlook
conta_secundaria = outlook.Session.Accounts["brunnomanducarfe@gmail.com"]

# conectando na conta secundaria
email._oleobj_.Invoke(*(64209, 0, 8, 0, conta_secundaria))

link_imagem = "https://i.ibb.co/5WDNHbbJ/logo-bm2.png"

email.To = "michi.oliveiraa@gmail.com"
email.Cc = "brunnomanducarfe+copia@gmail.com"
email.Subject = "Email enviado pelo Outlook"
email.Body = "Texto do E-mail"
email.HTMLBody = f"""
    <p>Meu primeiro parágrafo</p>
    <p>Outro parágrafo no e-mail.</p>
    <img src='{link_imagem}'>
"""

# pasta aonde esta rodando o codigo
caminho_codigo = os.getcwd()
# arquivo_anexar = "anexos/kivy.png"
# caminho_anexo = os.path.join(caminho_codigo, arquivo_anexar)
lista_arquivos_anexo = os.listdir("anexos")

for nome_arquivo in lista_arquivos_anexo:
    caminho_anexo = os.path.join(caminho_codigo, "anexos", nome_arquivo)
    email.Attachments.Add(caminho_anexo)

email.Send()
