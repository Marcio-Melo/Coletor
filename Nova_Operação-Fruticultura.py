from os.path import realpath, dirname
import pyautogui
import random
import keyboard
import pytest
import time

# Rolar para baixo imediatamente
# Este comando depende do sistema operacional (Ctrl + seta para baixo)
pyautogui.click(717, 246)
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

# Selecionar José damião
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para campo atividade principal
# Seleciona Fruticultura
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Clicar em Iniciar Operação
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
