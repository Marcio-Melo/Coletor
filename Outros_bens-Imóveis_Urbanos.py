from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.5)
pyautogui.hotkey('ctrl', 'end')

# Clicar em Adicionar Bem
pyautogui.click(1695,260, duration=0.5) 
pyautogui.moveTo(852,255, duration=0.5) 
# Ir para o campo Tipo do patrimônio
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar Imóveis Urbanos
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Matrícula
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('45549')
pyautogui.sleep(0.5)

# Ir para o campo Tipo do Imóvel (Casa)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar valor
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo UF
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar valor
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Município
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar valor
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Área útil (m²)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('45549')
pyautogui.sleep(0.5)

# Ir para o campo Valor por m² (R$/m²)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('84526')
pyautogui.sleep(0.5)

# Ir para o campo Valor de liquidação forçada (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('147457')
pyautogui.sleep(0.5)

# Ir para o campo Valor de liquidação forçada (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('João da Silva')
pyautogui.sleep(0.5)

# Ir para o botão salvar bem
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')