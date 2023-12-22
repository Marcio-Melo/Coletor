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

# clicar na tela
pyautogui.click(191,645)

# Clicar em pular
# ir para Botão Pular
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# ir para Botão Primeiro acesso
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# ir para Campo Primeiro Acesso de Usuário
pyautogui.hotkey('tab')
pyautogui.write('marcio')
pyautogui.sleep(0.3)

# ir para Campo CPF
pyautogui.hotkey('tab')
pyautogui.write('73308986272')
pyautogui.sleep(0.3)

# ir para Campo Nome
pyautogui.hotkey('tab')
pyautogui.write('marcio')
pyautogui.sleep(0.3)

# ir para Campo Senha
pyautogui.hotkey('tab')
pyautogui.write('marcio')
pyautogui.sleep(0.3)

# ir para Campo Confirme sua Senha
pyautogui.hotkey('tab')
pyautogui.write('marcio')
pyautogui.sleep(0.3)

# ir para Botão Primeiro Acesso
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')