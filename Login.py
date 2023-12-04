from os.path import realpath, dirname
import pyautogui
import random
import keyboard
import pytest
import time

# - Preenchimento da tela inicial e página de login
# INFORMAÇÕES GERAIS

# Clicar em pular
pyautogui.click(1726, 902, duration=1)



# Clicar e digitar meu usuário  
pyautogui.click(1557,555, duration=0.5)
pyautogui.write('marcio')

# Clicar e digitar minha senha
pyautogui.click(1383,664, duration=0.5)
pyautogui.write('marcio')

# Clicar no botão lembrar-me
pyautogui.click(1270,731, duration=0.5)

# Clicar em entrar
pyautogui.click(1333,802, duration=0.5)