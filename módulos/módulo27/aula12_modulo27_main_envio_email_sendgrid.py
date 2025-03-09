import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

# API

# - Requisições (requests, get, post, patch, delete)

# - Biblioteca (sendgrid)

chave_api_sendgrid = os.getenv("CHAVE_API_SENDGRID")

conta_sendgrid = SendGridAPIClient(chave_api_sendgrid)

email = Mail(from_email="brunnomanducarfe@gmail.com", 
             to_emails=['michi.oliveiraa@gmail.com', 'brunno.manduca@icloud.com', 'brunnomanducarfe+copia@gmail.com'], 
             subject="Email enviado pelo Sendgrid no Python", 
             html_content="<h1>Primeiro e-mail enviado pelo Sendgrid no Python!</h1><p style='color: #4d47c3'>Email enviado com sucesso, seja bem vindo</p><p color: #1debc9; text-decoration: underline;>Abraços e até o próximo e-mail.</p>")

resposta = conta_sendgrid.send(email)
print(resposta.status_code)
