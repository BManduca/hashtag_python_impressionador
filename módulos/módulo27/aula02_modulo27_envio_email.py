import os
import email.message
import smtplib
from dotenv import load_dotenv

load_dotenv()

email_senha = os.getenv("EMAIL_SENHA")

# smtp -> permite fazer a conexao para servidor do seu email 
# email.message -> biblioteca email é a que permite construir a mensagem de emails

# e-mail com anexo -> criar um e-mail de multipartes

def enviar_email():

    # Message() -> instância da classe message
    msg = email.message.Message()
    msg["Subject"] = "Email enviado com Python"
    msg["From"] = "brunnomanducarfe@gmail.com"
    msg["To"] = "michi.oliveiraa@gmail.com"
    msg["Cc"] = "brunnomanducarfe+copia@gmail.com"
    # msg["Bcc"] = "brunnomanducarfe@gmail.com"

    link_imagem = "https://i.ibb.co/8gjGHF8S/logo-bm-1.png"

    corpo_email = f"""
        <p>Boa tarde,</p>
        <p>Esse é o meu primeiro e-mail com Python usando smtplib</p>
        <p>Att., Brunno.</p>
        <img src='{link_imagem}' >
    """

    # padrão de código de textos de programação que permite caracteres com acentos ou até mesmo os especiais.
    corpo_email = corpo_email.encode("utf-8")

    # msg.add_header("Content-type", "text/html")
    msg.set_type("text/html") # garantindo que seja entendido como HTML
    msg.set_payload(corpo_email)


    # https://kinsta.com/pt/blog/servidor-smtp-gmail/

    
    """ conectando com servidor e-mail
    smtplib.SMTP("endereco_servidor", "porta")
    endereco_servidor -> link de endereco do servidor
    porta -> porta usada para fazer envio do e-mail """

    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        # starttls -> formato de criptografia que os email usam para enviar mensagem entre si
        servidor.starttls()
        servidor.login(msg["From"], email_senha)
        servidor.send_message(msg)
        servidor.quit()

        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f'Erro ao enviar o e-mail: {e}')

enviar_email()
