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

# Clicar no campo % Societário
pyautogui.click(1491, 685, duration=0.5)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('1')


# Clicar no botão Salvar Condomínio
pyautogui.click(1672, 852, duration=0.5)

# Clicar na Aba Principais Fornecedores
pyautogui.click(837, 307, duration=0.5)

# Clicar no campo Nome do Fornecedor
pyautogui.click(732, 491, duration=0.5)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('Sementes Plante')

# Clicar no campo Prazo Médio de Compras
pyautogui.click(1118, 496, duration=0.5)
# Pressionar Ctrl + A para selecionar todo o texto
# Pressionar Delete para apagar o texto selecionado
pyautogui.click(1213, 533, duration=0.5)


# Clicar no campo % Participação
pyautogui.click(1431, 494, duration=0.5)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('10000')

# Clicar no botão Salvar Principais Fornecedores
pyautogui.click(1657, 643, duration=0.5)

# Clicar na Principais Clientes
pyautogui.click(1049, 306, duration=0.5)

# Clicar no campo Nome do Cliente
pyautogui.click(757, 499, duration=0.5)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('São Salvador Alimentos')

# Botão com comportamento diferente (não aceita usar "Tab")
# Clicar no campo Prazo Médio de Compras
pyautogui.click(1118, 496, duration=0.5)
# Clicar em Semestral
pyautogui.click(1213, 533, duration=0.5)


# Clicar no campo % Participação
pyautogui.click(1431, 494, duration=0.5)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('10000')

# Clicar no botão SALVAR PRINCIPAIS CLIENTES
pyautogui.click(1677, 638, duration=0.5)

# Clicar na aba SEGURO RURAL
pyautogui.click(1211, 302, duration=0.5)

# Clicar no campo Seguro Rural
pyautogui.click(794, 497, duration=0.5)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('Seguro Agrícola - Custeio')
# ir para o campo seguradora
pyautogui.hotkey('tab')

# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('teste')
# ir para o campo seguradora
pyautogui.hotkey('tab')
# ir para o botão salvar seguro rural
pyautogui.hotkey('tab')
# Realizar o clique após a tecla "Tab"
pyautogui.hotkey('enter')

# Clicar na aba Selos e Certificações
pyautogui.click(1355, 307, duration=0.5)

# Clicar no campo Selos e Certificações
pyautogui.click(815, 502, duration=0.5)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('Brasil Certificado')

pyautogui.hotkey('tab')
# ir para o botão salvar seguro rural
pyautogui.hotkey('tab')
# Realizar o clique após a tecla "Tab"
pyautogui.hotkey('enter')

# Clicar na aba  Iniciativas Socioambientais
pyautogui.click(1530, 300, duration=0.5)

# Clicar no campo Iniciativas Socioambientais
pyautogui.click(815, 502, duration=0.5)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('Energia')

pyautogui.hotkey('tab')
# ir para o botão salvar Iniciativas Socioambientais
pyautogui.hotkey('tab')
# Realizar o clique após a tecla "Tab"
pyautogui.hotkey('enter')
