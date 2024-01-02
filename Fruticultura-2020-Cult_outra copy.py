from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time

# Rolar para baixo imediatamente
pyautogui.click(648, 721)
pyautogui.hotkey('ctrl', 'end')
pyautogui.sleep(0.3)

# Clicar botão Preencher ano (2020)
pyautogui.click(1092, 213)
pyautogui.sleep(0.3)

# Clicar no botão adicionar cultura (Outras)
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Clicar no botão Preencher (Outras)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para campo Produto (Cacau)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.sleep(0.3)

# Ir para campo Tipo (Sequeira e irrigada)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.sleep(0.3)

# Ir para campo Manejo (Pós-colheita)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para campo Nível tecnológico (Alto)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.sleep(0.3)

# Ir para botão Prosseguir
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)