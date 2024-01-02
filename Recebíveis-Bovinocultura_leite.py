from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time

# Rolar para baixo imediatamente
pyautogui.click(690,860)
pyautogui.hotkey('ctrl', 'end')
pyautogui.sleep(0.3)

# Clicar em Adicionar recebível
pyautogui.click(1140,246)
pyautogui.moveTo(690,860)
pyautogui.sleep(0.3)

# Ir para o campo Tipo de Produto
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

# Selecionar Tipo de Produto (Leite)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para o campo Comprador
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

keyboard.write('Banco do Brasil')
pyautogui.sleep(0.3)

# Ir para o campo Número do Contrato
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

keyboard.write('Banco do Brasil')
pyautogui.sleep(0.3)

# Ir para o campo Instrumento
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

# Selecionar CPR
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para o campo Quantidade (l/ano)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

keyboard.write('4100')
pyautogui.sleep(0.3)

# Ir para o campo Preço de venda (R$/l)
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

keyboard.write('2,02')
pyautogui.sleep(0.3)

# Ir para o campo Data da Entrega do Produto
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

keyboard.write('12022023')
pyautogui.sleep(0.3)

# Ir para o campo Data de Recebimento
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

keyboard.write('28022023')
pyautogui.sleep(0.3)

# Ir para botão Salvar Recebível
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

# Clicar no botão Salvar Recebível
pyautogui.hotkey('enter')