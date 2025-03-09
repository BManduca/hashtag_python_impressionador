# SMTP

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def enviar_email():
    
    msg = MIMEMultipart()
    msg["Subject"] = "Email enviado com Python"
    msg["From"] = "seuemail@gmail.com"
    msg["To"] = "seuemaildestino@gmail.com"
    msg["Cc"] = "seuemailcopia@gmail.com;outroemailcopia@hotmail.com"
    msg["Bcc"] = "seuemailcopiaoculta@gmail.com"
    
    link_imagem = "coloque_aqui_o_link_da_sua_imagem"

    corpo_email = f"""<p>Boa tarde,</p>
    <p>Esse é meu primeiro email com Python usando smtplib</p>
    <p>Att., Lira</p>
    <img src='{link_imagem}'>"""

    msg.attach(MIMEText(corpo_email, "html"))

    # anexar arquivos
    lista_arquivos = os.listdir("anexos")
    for nome_arquivo in lista_arquivos:
        with open(f"anexos/{nome_arquivo}", "rb") as arquivo:
            msg.attach(MIMEApplication(arquivo.read(), Name=nome_arquivo))

    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(msg["From"], "sua_senha_app_aqui")
    servidor.send_message(msg)
    servidor.quit()
    print("Email enviado")


enviar_email()