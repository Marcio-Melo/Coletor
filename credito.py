from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time

# - Preenchimento da aba Crédito:
# Crédito


def preencher_credito():
    # Rolar para baixo imediatamente
    pyautogui.click(477, 712)
    pyautogui.hotkey('ctrl', 'end')

    # Aguarde um curto período
    pyautogui.sleep(0.3)

    # Clicar no campo Valor solicitado
    pyautogui.click(587, 342)
    pyautogui.sleep(0.3)
    # Pressionar Ctrl + A para selecionar todo o texto
    pyautogui.hotkey('ctrl', 'a')
    # Pressionar Delete para apagar o texto selecionado
    keyboard.write('21220311')

    pyautogui.sleep(0.3)
    # Clicar no campo Descreva o detalhamento sobra a finalidade
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'a')
    # Pressionar Delete para apagar o texto selecionado
    keyboard.write(
        'Aquisição de matrizes e compra de insumos para produção de forrageiras.')
    pyautogui.sleep(0.3)

    # Ir para campo Prazo de Pagamento
    pyautogui.hotkey('tab')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.sleep(0.3)

    # Clicar no botão Salvar Crédito
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')

# Chamar a função para execução
preencher_credito()

# Tirar parênteses se quiser reproduzir somente esse script
