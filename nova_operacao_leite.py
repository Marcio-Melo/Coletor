from os.path import realpath, dirname
import pyautogui
import random
import keyboard
import pytest
import time

def nova_operacao():
    print("Esta é a minha função personalizada!")

    # Clicar no programa
    pyautogui.click(948, 294)
    # Clicar em Nova operação
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar na combo Solicitante
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar em Iniciar Operação
    pyautogui.hotkey('tab')

    # Clicar no botão Iniciar Operação
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

print("Função personalizada foi chamada!")
# Adicione qualquer lógica adicional conforme necessário