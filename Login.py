from os.path import realpath, dirname
import pyautogui
import random
import keyboard
import pytest
import time

'''
# CMD
# Python
# from mouseinfo import mouseInfo
# mouseInfo()
# desmarcar 3 sec delay
'''

# - Preenchimento da tela inicial e página de login
# INFORMAÇÕES GERAIS

# Clicar em pular
pyautogui.click(1726, 902)
#pyautogui.sleep(0.3)

# Clicar e digitar meu usuário  
pyautogui.click(1557,555)
pyautogui.write('marcio')
#pyautogui.sleep(0.3)

# Clicar e digitar minha senha
pyautogui.click(1383,664)
pyautogui.write('marcio')
#pyautogui.sleep(0.3)

# Clicar no botão lembrar-me
pyautogui.click(1270,731)
#pyautogui.sleep(0.3)

# Clicar em entrar
pyautogui.click(1333,802)