import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

# Credenciais do Outlook
EMAIL_OUTLOOK = "seuemail@outlook.com"
SENHA_OUTLOOK = os.getenv('var_senha')

EMAIL_TO = "michi.oliveiraa@gmail.com"

# Configuração do servidor SMTP do Outlook
SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587  # TLS

# Criar e-mail
destinatario = EMAIL_TO
assunto = "Teste de E-mail via Outlook no Mac"
corpo_email = """
        <p>Boa tarde,</p>
        <p>Enviando e-mail via Outlook utilizando biblioteca smtp</p>
        <p>Att., Brunno.</p>
    """

# Criando a mensagem
msg = MIMEMultipart()
msg["From"] = EMAIL_OUTLOOK
msg["To"] = EMAIL_TO
msg["Subject"] = assunto
msg.attach(MIMEText(corpo_email, "plain"))

try:
    # Conectar ao servidor SMTP do Outlook
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Iniciar segurança TLS
    server.login(EMAIL_OUTLOOK, SENHA_OUTLOOK)  # Autenticação
    server.sendmail(EMAIL_OUTLOOK, EMAIL_TO, msg.as_string())  # Enviar e-mail
    server.quit()  # Fechar conexão

    print("E-mail enviado com sucesso!")

except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")
