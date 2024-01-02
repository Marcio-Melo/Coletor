from os.path import realpath, dirname
import pyautogui
import random
import keyboard
import pytest
import time

from nova_operacao_leite import nova_operacao
from dados_solicitante import dados_solicitante
from credito import preencher_credito
from atividade_rural import preencher_rural


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
#pyautogui.click(1090,895)

# Clicar na outra tela
pyautogui.click(825, 293)

# Clicar e digitar meu usuário
pyautogui.hotkey('tab')
keyboard.write('marcio')
pyautogui.sleep(0.3)

# ir para campo senha e preencher
pyautogui.hotkey('tab')
keyboard.write('marcio')
pyautogui.sleep(0.3)

# Clicar no botão lembrar-me
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Clicar em entrar
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')

# Chame a função importada

nova_operacao()
dados_solicitante()

pyautogui.click(184, 360)

preencher_credito()

pyautogui.click(228, 424)
preencher_rural()