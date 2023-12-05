from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time

# - Preenchimento da aba Bovinocultura de leite:
# Atividade Rural
# Condomínio Agropecuário

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.5)
pyautogui.hotkey('ctrl', 'end')

# clicar no botão Adicionar Propriedade
pyautogui.click(1695,257, duration=0.5)

# clicar na combo Tipo da propriedade
pyautogui.click(1545,243, duration=0.5)

# selecionar Própria
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.5)

# Ir para o campo Matrícula
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para matrícula
keyboard.write('56451')
pyautogui.sleep(0.5)

# Ir para o campo CCIR
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para CCIR
keyboard.write('5641446841234')
pyautogui.sleep(0.5)

# Ir para o campo CAR
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para CAR
keyboard.write('AS5456')
pyautogui.sleep(0.5)

# Ir para o campo LATITUDE
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para LATITUDE
keyboard.write('85645')
pyautogui.sleep(0.5)

# Ir para o campo Longitude
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para Longitude
keyboard.write('85645')
pyautogui.sleep(0.5)

# Ir para o campo Nome da Fazenda
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para Nome da Fazenda
keyboard.write('85645')
pyautogui.sleep(0.5)

# Ir para o campo UF
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor UF
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo município
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor município
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Área Total (ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para Área Total (ha)
keyboard.write('85645')
pyautogui.sleep(0.5)

# Ir para o campo Área Produtiva (ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para Área Produtiva (ha)
keyboard.write('85645')
pyautogui.sleep(0.5)

# Ir para o campo Número de Safras por Ano
pyautogui.hotkey('tab')
# preencher valor para Número de Safras por Ano
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Área Irrigada (ha)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para Área Irrigada (ha)
keyboard.write('85645')
pyautogui.sleep(0.5)

# Ir para o campo Reserva Legal (ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para Reserva Legal (ha)
keyboard.write('85645')
pyautogui.sleep(0.5)

# Ir para o campo Atividade Principal
pyautogui.hotkey('tab')
# preencher valor Atividade Principal
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Valor Terra Nua/ha (R$)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para Valor Terra Nua/ha (R$)
keyboard.write('85645')
pyautogui.sleep(0.5)

# Ir para o campo Área Georeferenciada
pyautogui.hotkey('tab')
# preencher valor Área Georeferenciada (SIM)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Solo Predominante
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# preencher valor Solo Predominante 
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Sobreposição com Terras Indígenas, Assentamentos, Quilombolas ou Áreas de Conservação
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# preencher valor Sobreposição com Terras Indígenas, Assentamentos, Quilombolas ou Áreas de Conservação
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Cartório de Registro do Imóvel
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para Cartório de Registro do Imóvel
keyboard.write('85645')
pyautogui.sleep(0.5)

# Ir para o campo Sócios
pyautogui.hotkey('tab')
# preencher valor Sócios
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Hipoteca
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# preencher valor Hipoteca
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Alienação Fiduciária
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# preencher valor Alienação Fiduciária
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Confrontantes
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para Confrontantes
keyboard.write('85645')
pyautogui.sleep(0.5)

# Clicar no botão Salvar Propriedade
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)