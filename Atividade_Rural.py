from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time

# - Preenchimento da aba ATIVIDADE RURAL:
# Atividade Rural
# Condomínio Agropecuário

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.5)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(1)

# Clicar no campo Nome do Grupo
pyautogui.click(766, 477, duration=0.5)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('João Miguel da Silva')

# Clicar no campo Percentual societário do solicitante
pyautogui.click(1283, 472, duration=0.5)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('9999')

# Outros participantes da atividade
# Clicar no campo Nome Completo
pyautogui.click(777, 683, duration=0.5)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('Outra pessoa')

# Clicar no campo CPF / CNPJ
pyautogui.click(1078, 688, duration=0.5)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('03966695146')

