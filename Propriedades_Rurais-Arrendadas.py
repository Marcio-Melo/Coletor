from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time

# Rolar para baixo imediatamente
pyautogui.click(648,721)
pyautogui.hotkey('ctrl', 'end')
pyautogui.sleep(0.3)

# clicar no botão Adicionar Propriedade
pyautogui.click(1070,245)
pyautogui.sleep(0.3)

# clicar na combo Tipo da propriedade
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

# selecionar Arrendada
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.3)

# Ir para o campo Matrícula
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para matrícula
keyboard.write('56451')
pyautogui.sleep(0.3)

# Ir para o campo CCIR
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para CCIR
keyboard.write('5641446841234')
pyautogui.sleep(0.3)

# Ir para o campo CAR
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para CAR
keyboard.write('AS5456')
pyautogui.sleep(0.3)

# Ir para o campo LATITUDE
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para LATITUDE
keyboard.write('85645')
pyautogui.sleep(0.3)

# Ir para o campo Longitude
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para Longitude
keyboard.write('85645')
pyautogui.sleep(0.3)

# Ir para o campo Nome da Fazenda
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para Nome da Fazenda
keyboard.write('85645')
pyautogui.sleep(0.3)

# Ir para o campo Arrendatário
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para Arrendatário
keyboard.write('85645')
pyautogui.sleep(0.3)

# Ir para o campo UF
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor UF
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para o campo município
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor município
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para o campo Início Arrendamento
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor Início Arrendamento
keyboard.write('12122023')
pyautogui.sleep(0.3)

# Ir para o campo Término Arrendamento
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor Término Arrendamento
keyboard.write('27122023')
pyautogui.sleep(0.3)

# Ir para o campo Área Arrendada
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para Área Arrendada
keyboard.write('85645')
pyautogui.sleep(0.3)

# Ir para o campo Atividade Principal
pyautogui.hotkey('tab')
# preencher valor para Atividade Principal (cultivo de algodão)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para o campo Valor Total do Arrendamento (R$/ano)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para Valor Total do Arrendamento (R$/ano)
keyboard.write('85645')
pyautogui.sleep(0.3)

# Clicar no botão Salvar Propriedade
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)