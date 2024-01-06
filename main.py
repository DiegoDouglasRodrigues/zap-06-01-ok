from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import urllib
import os


navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com")
#enviar a mensagem

while len(navegador.find_elements(By.ID, 'side')) < 1:  # elemento que diz que que a tela carregou
    time.sleep(1)

time.sleep(2)  # garantia

# Whatsapp ja carregou
tabela = pd.read_excel("Envios.xlsx")
#print(tabela[['nome', 'mensagem', 'arquivo']])

lista_rotas = ['g', 'AB', 'b', 'F', 'x']

for linha in tabela.index:
    carga = tabela.loc[linha,"carga"]
    nome = tabela.loc[linha, "nome"]
    mensagem = tabela.loc[linha, "mensagem"]
    mensagem2 = tabela.loc[linha, "mensagem2"]
    arquivo = tabela.loc[linha, "arquivo"]
    telefone = tabela.loc[linha, "telefone"]
    whatasapp = tabela.loc[linha, "whatsapp"]
    print(f'#############{whatasapp}')

    # Substituir "Cliente" pelo nome
    texto = mensagem.replace("Cliente", nome)
    # Substituir "*" por dois caracteres de nova linha
    texto = texto.replace("*", '\n\n')

    # Substituir "Cliente" pelo nome
    texto2 = mensagem2.replace("Cliente", nome)
    # Substituir "*" por dois caracteres de nova linha
    texto2 = texto2.replace("*", '\n\n')



    lista_rotas = [rota.upper() for rota in lista_rotas]

    #print(whatasapp)

# verificando se é carga do dia
    if carga in lista_rotas:
        print(carga)




    #definindo a primeira opção de mensagem
        if whatasapp == 1:
            texto = mensagem.replace("Cliente", nome)
            # Substituir "*" por dois caracteres de nova linha
            texto = texto.replace("*", '\n\n')
            print(f'mensagem 1 {texto}')
            print('**************************')
            texto = urllib.parse.quote(texto)
            # print(texto)

            # enviar a mensagem
            link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"

            navegador.get(link)
            print(' peguei o link')

            # esperar a tela do whatsapp carregar -> espera um elemento que só existe na tela já carregada aparecer
            while len(navegador.find_elements(By.ID,
                                              'side')) < 1:  # -> lista for vazia -> que o elemento não existe ainda
                time.sleep(2)
            time.sleep(2)  # só uma garantia

            print('antes do numero invalido')
            # você tem que verificar se o número é inválido
            if len(navegador.find_elements(By.XPATH,
                                           '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
                time.sleep(2)
            time.sleep(1)

            print('1 aguardar')
            # esperar a tela do whatsapp carregar -> espera um elemento que só existe na tela já carregada aparecer
            while len(navegador.find_elements(By.XPATH,
                                              '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[1]/button[2]/div/span')) < 1:  # -> lista for vazia -> que o elemento não existe ainda
                # '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[1]/button/span'
                # '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[1]/button[2]/div/span'
                time.sleep(1)
            time.sleep(2)  # só uma garantia

            print('antes do click')

            # enviar a mensagem
            navegador.find_element(By.XPATH,
                                   '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()

            print('pos click')

            if arquivo != "N":
                caminho_completo = os.path.abspath(f"arquivos/{arquivo}")
                navegador.find_element(By.XPATH,
                                       '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click()
                navegador.find_element(By.XPATH,
                                       '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button/input').send_keys(
                    caminho_completo)
                time.sleep(2)
                navegador.find_element(By.XPATH,
                                       '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()

            print('pos ultimo if')
            time.sleep(5)

        # print('acabou')

        # 06/01







    #definindo a Segunda opção de mensagem
        if whatasapp == 2:
            texto2 = mensagem2.replace("Cliente", nome)
            # Substituir "*" por dois caracteres de nova linha
            texto2 = texto2.replace("*", '\n\n')
            print(f'mensagem 2 {texto2}')
            print('**************************')



            texto2 = urllib.parse.quote(texto2)
            #print(texto2)

            # enviar a mensagem
            link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto2}"

            navegador.get(link)
            print(' peguei o link')

            # esperar a tela do whatsapp carregar -> espera um elemento que só existe na tela já carregada aparecer
            while len(navegador.find_elements(By.ID, 'side')) < 1:  # -> lista for vazia -> que o elemento não existe ainda
                time.sleep(2)
            time.sleep(2)  # só uma garantia

            print('antes do numero invalido')
            # você tem que verificar se o número é inválido
            if len(navegador.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
                time.sleep(2)
            time.sleep(1)

            print('1 aguardar')
            # esperar a tela do whatsapp carregar -> espera um elemento que só existe na tela já carregada aparecer
            while len(navegador.find_elements(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[1]/button[2]/div/span')) < 1:  # -> lista for vazia -> que o elemento não existe ainda
                                                        #'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[1]/button/span'
                                                        #'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[1]/button[2]/div/span'
                time.sleep(1)
            time.sleep(2)  # só uma garantia

            print('antes do click')


            # enviar a mensagem
            navegador.find_element(By.XPATH,
                                   '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()

            print('pos click')

            if arquivo != "N":
                caminho_completo = os.path.abspath(f"arquivos/{arquivo}")
                navegador.find_element(By.XPATH,
                                       '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click()
                navegador.find_element(By.XPATH,
                                       '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button/input').send_keys(
                    caminho_completo)
                time.sleep(2)
                navegador.find_element(By.XPATH,
                                       '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()

            print('pos ultimo if')
            time.sleep(5)

    #print('acabou')

    #06/01

    # commit publico