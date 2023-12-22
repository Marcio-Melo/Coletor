from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.5)
pyautogui.hotkey('ctrl', 'end')

# Clicar em Adicionar recebível 
pyautogui.click(1695,260, duration=0.5)
pyautogui.moveTo(852,255, duration=0.5)

# Ir para o campo Tipo de Produto
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar Tipo de Produto (Leite)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Comprador
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('Banco do Brasil')
pyautogui.sleep(0.5)

# Ir para o campo Número do Contrato
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('Banco do Brasil')
pyautogui.sleep(0.5)

# Ir para o campo Instrumento
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)

# Selecionar CPR
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Quantidade (l/ano)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('4100')
pyautogui.sleep(0.5)

# Ir para o campo Preço de venda (R$/l)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('2,02')
pyautogui.sleep(0.5)

# Ir para o campo Data da Entrega do Produto
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('12022023')
pyautogui.sleep(0.5)

# Ir para o campo Data de Recebimento
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('28022023')
pyautogui.sleep(0.5)

# Ir para botão Salvar Recebível
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)

# Clicar no botão Salvar Recebível
pyautogui.hotkey('enter')