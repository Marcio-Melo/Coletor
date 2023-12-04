from os.path import realpath, dirname
import pyautogui
from time import sleep


# 4 - Extrair cada produto
with open('dados_solicitante.txt', 'r') as arquivo:
    for linha in arquivo:
        valores = linha.strip().split(',')
        
        if len(valores) >= 3:
            produto = valores[0]
            quantidade = valores[1]
            preco = valores[2]

            # 	1 - Clicar e digitar produto
            pyautogui.click(735, 527, duration=1)
            pyautogui.write(produto)
            
            # 	2 - Clicar e digitar quantidade
            pyautogui.click(696, 558, duration=1)
            pyautogui.write(quantidade)
            
            # 	3 - Clicar e digitar preço
            pyautogui.click(679, 581, duration=1)
            pyautogui.write(preco)