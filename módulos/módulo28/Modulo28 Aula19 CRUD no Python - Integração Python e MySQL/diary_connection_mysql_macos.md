# Instalando o MySQL Server no MacOS

## Passo1: Baixar o MySQL Server

1. Acesse o site oficial do MySQL:
   1. 👉 [https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/)
2. Efetuar Download da versão do MySQl Server para MacOS(macOS "versão" ARM ou Intel, dependendo do chip que está sendo utilizado).
3. Selecione o DMG Archive para instalação via interface gráfica.
4. Efetue Download (Pode ignorar o login/registro clicando em "No thanks, just start my download.")


## Passo 2: Instalando MySQL Server

1. Abra o arquivo .dmg baixado
2. Siga o assistente de instalação clicando em Continuar > Aceitar > Instalar.
3. No final da instalação, o sistema vai pedir que gere uma senha temporária para o usuário root. **Anote esse senha**, pois será necessária na primeira conexão.
4. A opção **"Start MySQL Server on Startup"** pode aparecer. Marque se quiser que o MySQL inicie automaticamente com o MacOS.
5. Conclua a instalação.


## Passo 3: Iniciar o MySQL Server (se necessário)

* Vá em **Preferências do Sistema > MySQL.**
* Clique em **Start MySQL Server** (caso ele não esteja rodando).

    ⚙️**Alternativa via Terminal** **:**

    ``sudo /usr/local/mysql/support-files/mysql.server start``


---



# Instalando o MySQL Workbench

## Passo1: Baixar o MySQL Workbench

1. Acesse:
   1. 👉 [https://dev.mysql.com/downloads/workbench/](https://dev.mysql.com/downloads/workbench/)
2. Baixe a versão compatível com o seu MacOS (ARM ou Intel)
3. Instale o Workbench arrastando o ícone para a pasta **Aplicativos**


---



# Fazendo conexão com o MySQL Workbench

## Passo 1: Abrir o Workbench

1. Abra o MySQL Workbench na pasta **Aplicativos**
2. Clique em + (Add Connection) no canto inferior esquerdo

## Passo 2: Configurar a conexão

* **Connection Name:** Nome que você desejar (ex.: Local MySQL)
* **Connection Method:** Standard (TCP/IP)
* **Hostname:** 127.0.0.1 ou localhost
* **Port:** 3306 (porta padrão do MySQL)
* **Username:** root
* **Password:** Clique em **Store in Keychain..** e insira a senha temporária gerada na instalação. (Esta senha pode ser mudada depois com ALTER USER)

## Passo 3: Testar conexão

1. Clique em **Test Connection.**
2. Se aparecer "Successfully made the MySQL connection", está tudo certo!


---



# (Opcional) Alterar a senha do root

1. Depois de conectar via Workbench ou terminal, pode ser bom **alterar a senha do usuário root:**
   1. **Via terminal**

      ```
      mysql -u root -p
      ```
   2. Depois, dentro do prompt **MySQL:**

      ```
      ALTER USER 'root'@'localhost' IDENTIFIED BY 'NovaSenhaForte@123&';
      FLUSH PRIVILEGES;
      EXIT;
      ```

      * Agora, use essa nova senha nas próximas conexões


---



# Testar com banco simples (opcional)

```
CREATE DATABASE teste;

USE teste;

CREATE TABLE usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(100), email VARCHAR(100));

INSERT INTO usuarios (nome, email) VALUES ('João da Silva', 'joao@mail.com');

SELECT * FROM usuarios;

```
