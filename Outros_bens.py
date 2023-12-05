from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time

# - Preenchimento da aba Bovinocultura de leite:
# Atividade Rural
# Condomínio Agropecuário

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.5)
pyautogui.hotkey('ctrl', 'end')

# clicar no botão Adicionar Propriedade
pyautogui.click(1695,257, duration=0.5)

# clicar na combo Tipo da propriedade
pyautogui.click(1545,243, duration=0.5)

# selecionar Própria
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.5)

# Ir para o campo Matrícula
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para matrícula
keyboard.write('56451')
pyautogui.sleep(0.5)

# Ir para o campo CCIR
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para CCIR
keyboard.write('5641446841234')
pyautogui.sleep(0.5)

# Ir para o campo CAR
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para CAR
keyboard.write('AS5456')
pyautogui.sleep(0.5)

# Ir para o campo LATITUDE
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para LATITUDE
keyboard.write('85645')
pyautogui.sleep(0.5)

# Ir para o campo Longitude
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para Longitude
keyboard.write('85645')
pyautogui.sleep(0.5)

# Ir para o campo Nome da Fazenda
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para Nome da Fazenda
keyboard.write('85645')
pyautogui.sleep(0.5)

# Ir para o campo UF
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor UF
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

