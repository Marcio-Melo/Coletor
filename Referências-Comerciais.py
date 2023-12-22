from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time

# Clicar em adicionar referências
pyautogui.click(1703, 602, duration=0.5)
pyautogui.moveTo(852, 255, duration=0.5)

# Ir para o campo Tipo da Referência
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar Tipo de Produto (Bancos e Fundos)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Nome
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('João Oliveira')
pyautogui.sleep(0.5)

# Ir para o campo Cargo
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('Gerente')
pyautogui.sleep(0.5)

# Ir para o campo Empresa
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('Banco do Brasil')
pyautogui.sleep(0.5)

# Ir para o campo E-mail
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('joaooliveira@gmail.com')
pyautogui.sleep(0.5)

# Ir para o campo Telefone
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('61981226537')
pyautogui.sleep(0.5)

# Ir para o botão salvar referência
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
pyautogui.hotkey('enter')
