from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time


def preencher_rural():
    # Rolar para baixo imediatamente

    pyautogui.click(598, 630)
    pyautogui.hotkey('ctrl', 'end')
    pyautogui.sleep(0.3)

    # Clicar no campo Nome do Grupo
    pyautogui.click(499, 294)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    keyboard.write('não tem')
    pyautogui.sleep(0.3)

    # Clicar no campo Percentual societário do solicitante
    pyautogui.hotkey('tab')
    keyboard.write('9999')
    pyautogui.sleep(0.3)

    # Outros participantes da atividade

    # Clicar no campo Nome Completo
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'a')
    keyboard.write('Outra pessoa')
    pyautogui.sleep(0.3)

    # Clicar no campo CPF / CNPJ
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'a')
    keyboard.write('03966695146')
    pyautogui.sleep(0.3)

    # Clicar no campo % Societário
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'a')
    keyboard.write('1')
    pyautogui.sleep(0.3)

    # Clicar no botão Salvar Condomínio
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar na Aba Principais Fornecedores
    pyautogui.click(689, 292)
    pyautogui.sleep(0.3)

    # Clicar no campo Nome do Fornecedor
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'a')
    keyboard.write('Sementes Plante')
    pyautogui.sleep(0.3)

    # Clicar no campo Prazo Médio de Compras
    pyautogui.hotkey('tab')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar no campo % Participação
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    keyboard.write('10000')
    pyautogui.sleep(0.3)

    # Clicar no botão Salvar Principais Fornecedores
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar na Principais Clientes
    pyautogui.click(876, 297)
    pyautogui.sleep(0.3)

    # Clicar no campo Nome do Cliente
    pyautogui.hotkey('tab')
    keyboard.write('São Salvador Alimentos')
    pyautogui.sleep(0.3)

    # Clicar no campo Prazo Médio de Compras
    pyautogui.hotkey('tab')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar no campo % Participação
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    keyboard.write('10000')
    pyautogui.sleep(0.3)

    # Clicar no botão SALVAR PRINCIPAIS CLIENTES
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar na aba SEGURO RURAL
    pyautogui.click(1006, 298)
    pyautogui.sleep(0.3)

    # Clicar no campo Seguro Rural
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    keyboard.write('Seguro Agrícola - Custeio')
    pyautogui.sleep(0.3)

    # ir para o campo seguradora
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'a')
    keyboard.write('teste')
    pyautogui.sleep(0.3)

    # ir para o botão salvar seguro rural
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar na aba Selos e Certificações
    pyautogui.click(1121, 296)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'a')
    keyboard.write('Brasil Certificado')
    pyautogui.sleep(0.3)

    # Ir para botão Salvar Selos e Certificações
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar na aba Iniciativas Socioambientais
    pyautogui.click(1123, 302)
    pyautogui.press('right')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar no campo Iniciativas Socioambientais
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'a')
    keyboard.write('Energia')
    pyautogui.sleep(0.3)

    # Ir para botão salvar iniciativas socioambientais
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

preencher_rural()
# Tirar parênteses se quiser reproduzir somente esse script
