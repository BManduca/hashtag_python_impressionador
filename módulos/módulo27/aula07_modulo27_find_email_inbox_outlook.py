import os
import win32com.client as win32

outlook = win32.Dispatch("outlook.application")

# MAPI -> protocolo de recebimento de email
caixas_emails = outlook.GetNamespace("MAPI")

# verificando quais contas existem denro do outlook
# for pasta in caixas_emails.Folders:
#     print(pasta)

# índice passado como parâmetro para o Item(), corresponde a qual conta e-mail estamos acessando
pasta_email_selecionado = caixas_emails.Folders.Item(2)

# verificando as subpastas presentes dentro da conta de email selecionada
# for subpasta in pasta_email_selecionado.Folders:
#     print(subpasta)

caixa_entrada = pasta_email_selecionado.Folders.Item(1)

lista_emails = caixa_entrada.Items

# print(len(lista_emails))

for i, email in enumerate(lista_emails, start=1):
    anexos = email.Attachments
    if email.To == "michi.oliveiraa@gmail.com" and len(anexos) > 0:
        print(email.Subject)
        print(email.Cc)
        print(email.Body)
        for anexo in anexos:
            print(anexo.FileName)
            caminho_codigo = os.getcwd()
            caminho_anexo_salvar = os.path.join(caminho_codigo, "anexos", f"Email_{i}_{anexo.FileName}")
            anexo.SaveAsFile(caminho_anexo_salvar)

print("Fim do programa.")
