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
# pyautogui.click(1726, 902)

# Clicar e digitar meu usuário
pyautogui.click(894, 574)
keyboard.write('marcio')
# pyautogui.sleep(0.3)

# ir para campo senha e preencher
pyautogui.hotkey('tab')
keyboard.write('marcio')
# pyautogui.sleep(0.3)

# Clicar no botão lembrar-me
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
# pyautogui.sleep(0.3)

# Clicar em entrar
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
