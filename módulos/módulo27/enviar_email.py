# SMTP

import smtplib
import email.message

def enviar_email():
    
    msg = email.message.Message()
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

    corpo_email = corpo_email.encode("utf-8")

    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpo_email)

    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(msg["From"], "sua_senha_app")
    servidor.send_message(msg)
    servidor.quit()
    print("Email enviado")


enviar_email()