from os.path import realpath, dirname
import pyautogui
import random
import keyboard
import pytest
import time

# Rolar para baixo imediatamente
# Este comando depende do sistema operacional (Ctrl + seta para baixo)
pyautogui.click(1616, 320, duration=0.5)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(1)

# Clicar em Nova operação
pyautogui.click(1638,291, duration=0.5)

# Clicar na combo Solicitante
pyautogui.click(1570,290, duration=0.5)

# Clicar na opção (Expedito)
pyautogui.click(1402, 594, duration=1)

# Atividade Principal já setada (Bovinocultura de leite)

# Clicar em Iniciar Operação
pyautogui.click(1548, 630, duration=2)