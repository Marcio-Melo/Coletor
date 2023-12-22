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
# Selecionar Aplicações financeiras
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Instituição Financeira
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar Aplicações financeiras
keyboard.write('Banco do Brasil')
pyautogui.sleep(0.5)

# Ir para o campo Tipo de Aplicação
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar Aplicações financeiras (CDB)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')    
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Valor da Aplicação (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar Aplicações financeiras
keyboard.write('500000')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)

# Clicar no botão Salvar Bem
pyautogui.hotkey('enter')