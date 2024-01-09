import pyautogui
import pandas as pd
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

#Importar a base de produtos
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.PAUSE= 0.3

#Abrir o navagedor (chrome)

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#Entrar no link

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/logi"

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

