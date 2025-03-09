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

for i, email in enumerate(lista_emails, start=1):
    print(' ')
    print('=' * 50)
    print(f"E-mail {i}")
    print('=' * 50)
    print(f"📩 Destinatário: {', '.join(email.to)}")
    print(f"📌 Assunto: {email.subject}")
    print(f"📅 Data: {email.date}")
    print("✉️  Corpo do E-mail:")
    print("-" * 50)
    print(email.text)
    print("-" * 50)

    if email.attachments:
        print("📎 Anexos encontrados: ")
        for anexo in email.attachments:
            # definindo o caminho completo para salvar o anexo
            caminho_anexo = os.path.join(pasta_anexos, f"Email_{i}_{anexo.filename}")
            with open(caminho_anexo, "wb") as arquivo:
                arquivo.write(anexo.payload)
            print(f"   ✔ Anexo salvo com sucesso => {caminho_anexo}")
    else:
        print("📂 Nenhum anexo encontrado...")

    print("=" * 50)
    print(' ')
