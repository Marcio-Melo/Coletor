from os.path import realpath, dirname
import pyautogui
import random
import keyboard
import pytest
import time

# Rolar para baixo imediatamente
# Este comando depende do sistema operacional (Ctrl + seta para baixo)
pyautogui.click(1616, 320, duration=0.3)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(0.3)

# Clicar em Nova operação
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')

# Clicar na combo Solicitante
pyautogui.sleep(0.3)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
pyautogui.hotkey('down')
# Seleciona Cosme Moraes
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para campo atividade principal
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
pyautogui.hotkey('down')
pyautogui.sleep(0.3)
# Seleciona Bovinocultura de leite
pyautogui.hotkey('down')
pyautogui.hotkey('enter')

# Clicar em Iniciar Operação
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')