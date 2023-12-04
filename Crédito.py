from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time

# - Preenchimento da aba Crédito:
# Crédito

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.5)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(1)

# Clicar no campo Valor solicitado
pyautogui.click(711, 357, duration=0.5)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
pyautogui.write('21220311')

# Clicar no campo Descreva o detalhamento sobra a finalidade
pyautogui.click(761, 465, duration=0.5)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write(
    'Aquisição de matrizes e compra de insumos para produção de forrageiras.')

# Clicar no botão Salvar Crédito
pyautogui.click(1704, 667, duration=0.5)
