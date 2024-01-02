from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time
# Seu arquivo principal ou outro arquivo Python

# Importe a função do arquivo minha_funcao_personalizada.py
from minha_funcao_personalizada import minha_funcao

# Rolar para baixo imediatamente
pyautogui.click(948,294)
pyautogui.hotkey('ctrl', 'end')
pyautogui.sleep(0.3)

# Clicar em Adicionar Bem
pyautogui.click(1086,244)
pyautogui.sleep(0.3)
# Ir para o campo Tipo do patrimônio
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# Selecionar Aplicações financeiras
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para o campo Instituição Financeira
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# Selecionar Aplicações financeiras
keyboard.write('Banco do Brasil')
pyautogui.sleep(0.3)

# Ir para o campo Tipo de Aplicação
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# Selecionar Aplicações financeiras (CDB)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')    
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para o campo Valor da Aplicação (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# Selecionar Aplicações financeiras
keyboard.write('500000')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

# Clicar no botão Salvar Bem
pyautogui.hotkey('enter')

# Seu código existente...

# Rolar para baixo imediatamente
pyautogui.click(648, 721)
# ... (restante do seu código)


# Chame a função importada
minha_funcao()