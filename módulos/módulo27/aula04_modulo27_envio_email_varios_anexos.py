import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
from dotenv import load_dotenv

load_dotenv()

email_senha = os.getenv("EMAIL_SENHA")
# e-mail com anexo -> para criar um e-mail com anexo, e feito um email multipartes

def enviar_email():

    msg = MIMEMultipart()
    msg["Subject"] = "Email enviado com Python"
    msg["From"] = "brunnomanducarfe@gmail.com"
    msg["To"] = "michi.oliveiraa@gmail.com"
    msg["Cc"] = "brunnomanducarfe+copia@gmail.com"
    # msg["Bcc"] = "brunnomanducarfe@gmail.com"

    link_imagem = "https://i.ibb.co/5WDNHbbJ/logo-bm2.png"

    corpo_email = f"""
        <p>Boa tarde,</p>
        <p>Esse é o meu primeiro e-mail com Python usando smtplib</p>
        <p>Att., Brunno.</p>
        <img src='{link_imagem}' >
    """

    msg.attach(MIMEText(corpo_email, "html"))

    # anexando arquivos
    lista_arquivos = os.listdir("anexos")

    for nome_arquivo in lista_arquivos:
        with open(f"anexos/{nome_arquivo}", "rb") as arquivo:
            msg.attach(MIMEApplication(arquivo.read(), Name=nome_arquivo))

    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(msg["From"], email_senha)
        servidor.send_message(msg)
        servidor.quit()

        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f'Erro ao enviar o e-mail: {e}')

enviar_email()
