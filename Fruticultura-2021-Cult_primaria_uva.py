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

# Clicar botão Preencher ano (2021)
pyautogui.click(1101,283)
pyautogui.sleep(0.3)

# Clicar no botão Preencher (Cultura Primária)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para campo Produto (Uva)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.sleep(0.3)

# Ir para campo Tipo (Sequeira)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.sleep(0.3)

# Ir para campo Manejo (Adubação)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para campo Nível tecnológico (Baixo)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.sleep(0.3)

# Ir para botão Prosseguir
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)