import os
# from pathlib import Path
from dotenv import load_dotenv
from imap_tools import AND, MailBox

load_dotenv()

email_usuario = "brunnomanducarfe@gmail.com"
email_senha = os.getenv("EMAIL_SENHA")

# criando a pasta para armazenar os anexos, caso a mesma não existir
# Path("anexos_emails/").mkdir(parents=True, exist_ok=True)
pasta_anexos = "anexos_emails"
os.makedirs(pasta_anexos, exist_ok=True)

# Conectando a caixa de entrada do email
meu_email = MailBox("imap.gmail.com").login(email_usuario, email_senha)

# vizualizando as pastas do meu email disponiveis
# for pasta in meu_email.folder.list():
#     print(pasta)

# meu_email.folder.set('[Gmail]/E-mails enviados')

# Buscar e-mails enviados para um destinatario específico
lista_emails = meu_email.fetch(AND(from_="brunnomanducarfe@gmail.com", to="michi.oliveiraa@gmail.com"))

for i, email in enumerate(lista_emails):
    if len(email.attachments) > 0:
        print(
            f"Destinatário email: {email.to}\nAssunto email: {email.subject}\nCorpo email: {email.text}\nData: {email.date}\n\n"
        )
        for anexo in email.attachments:
            print(f"Anexo: {anexo.filename}")
