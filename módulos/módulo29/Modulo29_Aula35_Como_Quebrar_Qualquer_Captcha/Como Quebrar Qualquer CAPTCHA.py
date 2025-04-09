import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from anticaptchaofficial.recaptchav2proxyless import *
from chave import chave_api

navegador = webdriver.Chrome()
link = "https://google.com/recaptcha/api2/demo"
navegador.get(link)

chave_captcha = navegador.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey')

solver = recaptchaV2Proxyless()
# verbose(1) -> efetua um retorno atualizando status para o user
solver.set_verbose(1)
# chave api enviada por email
solver.set_key(chave_api)
solver.set_website_url(link)
solver.set_website_key(chave_captcha)

resposta = solver.solve_and_return_solution()

if resposta != 0:
    print(resposta)
    # preencher o campo do token do captcha
    # g-recaptcha-response
    # encontrando o elemento pelo ID na página e preenchendo o mesmo com o conteudo presente na variável 'resposta'
    navegador.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
    navegador.find_element(By.ID, 'recaptcha-demo-submit').click()
else:
    print(solver.err_string)

time.sleep(100)
