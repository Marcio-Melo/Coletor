from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.5)
pyautogui.hotkey('ctrl', 'end')

# Clicar em Cadastrar endividamento
pyautogui.click(1695,260, duration=0.5)
pyautogui.moveTo(852,255, duration=0.5)

# Ir para o campo Tipo de Produto
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar Tipo de Produto (Bancos e Fundos)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Instituição Financeira
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('Banco do Brasil')
pyautogui.sleep(0.5)

# Ir para o campo Modalidade
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar Modalidade (ACC)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Garantia
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar Garantia (Alienação Fiduciária de Imóvel Rural)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Tomador do financiamento
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('Banco do Brasil')
pyautogui.sleep(0.5)

# Ir para o Prazo de Carência
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar (sem Carência)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o Campo Forma de pagamento
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar (Única)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o Campo Moeda
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Selecionar (Real)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Valor do financiamento
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('15324632')
pyautogui.sleep(0.5)

# Ir para o campo Taxa de Juros (% a.a.)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('521')
pyautogui.sleep(0.5)

# Ir para o campo Valor das parcelas
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('542384')
pyautogui.sleep(0.5)

# Ir para o campo Nº de parcelas restantes
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('234')
pyautogui.sleep(0.5)

# Ir para o campo Último Vencimento
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar
keyboard.write('22122023')
pyautogui.sleep(0.5)

# Ir para o botão Salvar Endividamento
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
pyautogui.hotkey('enter')