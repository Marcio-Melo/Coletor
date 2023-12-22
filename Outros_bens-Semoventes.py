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
# Selecionar Semoventes
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Especificação do Rebanho
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('gados')
pyautogui.sleep(0.5)

# Ir para o campo Peso Médio (Kg)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('30000')
pyautogui.sleep(0.5)

# Ir para o campo Quantidade (cab.)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('9200')
pyautogui.sleep(0.5)

# Ir para o campo Quantidade (cab.)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('230000')
pyautogui.sleep(0.5)

# Ir para o botão salvar bem
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')