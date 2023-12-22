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
# Selecionar Armazens
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

# Ir para o campo CCIR
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('120')
pyautogui.sleep(0.5)

# Ir para o campo Nome do armazém
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('Armazém do Jucá')
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

# Ir para o campo Tipo
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar valor (Armazém convencional)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Área Construída (m²)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('756423')
pyautogui.sleep(0.5)

# Ir para o campo Capacidade estática de armazenagem (ton)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('47814')
pyautogui.sleep(0.5)

# Ir para o campo Valor de mercado (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('30041581')
pyautogui.sleep(0.5)

# Ir para o campo Hipoteca
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar valor (Sim)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Alinação Fiduciária
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar valor (Sim)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Proprietário(s)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('sócio do governo')
pyautogui.sleep(0.5)

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)