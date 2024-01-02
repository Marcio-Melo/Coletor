from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time


def dados_solicitante():
    print("Esta é a minha função personalizada!")
    # Rolar para baixo imediatamente
    # Este comando depende do sistema operacional (Ctrl + seta para baixo)
    pyautogui.click(717, 394)
    pyautogui.hotkey('ctrl', 'end')
    pyautogui.sleep(0.3)

    # Clicar em Informações gerais
    pyautogui.click(500, 303)
    pyautogui.sleep(0.3)

    # Clicar no campo RG e preencher
    pyautogui.hotkey('tab')
    keyboard.write('4226134')
    pyautogui.sleep(0.3)

    # Clicar no campo Orgão/UF e Preencher
    pyautogui.hotkey('tab')
    keyboard.write('DGPC GO')
    pyautogui.sleep(0.3)

    # Clicar no campo Data de Emissão e preencher
    pyautogui.hotkey('tab')
    keyboard.write('12/09/1999')
    pyautogui.sleep(0.3)

    # Clicar no campo Nacionalidade e preencher
    pyautogui.hotkey('tab')
    keyboard.write('Brasileiro')
    pyautogui.sleep(0.3)

    # Clicar no campo Naturalidade e preencher
    pyautogui.hotkey('tab')
    keyboard.write('Goiás')
    pyautogui.sleep(0.3)

    # Clicar no campo Telefone e preencher
    pyautogui.hotkey('tab')
    keyboard.write('(62) 99982-1750')
    pyautogui.sleep(0.3)

    # Clicar no campo E-mail e preencher
    pyautogui.hotkey('tab')
    keyboard.write('miguelzinhobaiano@gmail.com')
    pyautogui.sleep(0.3)

    # Clicar no campo Data de Nascimento e preencher
    pyautogui.hotkey('tab')
    keyboard.write('09/06/1982')
    pyautogui.sleep(0.3)

    # Clicar no botão Salvar Informações Gerais
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # ABA ENDEREÇO
    # Clicar na aba ENDEREÇO
    pyautogui.click(577, 297)
    pyautogui.sleep(0.3)
    pyautogui.moveTo(366, 911)

    # Clicar no campo CEP
    pyautogui.hotkey('tab')
    keyboard.write('76630-000')
    pyautogui.sleep(0.3)

    # Clicar no campo UF
    pyautogui.hotkey('tab')
    pyautogui.hotkey('down')
    pyautogui.sleep(0.3)
    pyautogui.hotkey('down')
    pyautogui.sleep(0.3)
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar no campo Município
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.sleep(0.3)
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar no campo ENDEREÇO
    pyautogui.hotkey('tab')
    keyboard.write('Rua Luiz Antonio - QD 26 LT 32 - Centro')
    pyautogui.sleep(0.3)

    # Clicar no campo BAIRRO
    pyautogui.hotkey('tab')
    keyboard.write('não tem')
    pyautogui.sleep(0.3)

    # Clicar no campo NÚMERO
    pyautogui.hotkey('tab')
    keyboard.write('não tem')
    pyautogui.sleep(0.3)

    # Clicar no campo COMPLEMENTO
    pyautogui.hotkey('tab')
    keyboard.write('não tem')
    pyautogui.sleep(0.3)

    # Clicar no campo TEMPO DE RESIDÊNCIA NO MUNICÍPIO
    pyautogui.hotkey('tab')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar em SALVAR ENDEREÇO
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar na aba ATIVIDADE
    pyautogui.click(682, 294)

    # Clicar no campo Nome da Propriedade
    pyautogui.hotkey('tab')
    # Pressionar Ctrl + A para selecionar todo o texto
    pyautogui.hotkey('ctrl', 'a')
    # Pressionar Delete para apagar o texto selecionado
    keyboard.write('Fazenda Bom Futura')
    pyautogui.sleep(0.3)

    # Clicar no campo TEMPO DE EXERCÍCIO NESSA ATIVIDADE (ANOS)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar no campo PRINCIPAL UF DE ATUAÇÃO
    pyautogui.hotkey('tab')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar no campo Principal Município de Atuação
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar no campo Perfil do Produtor
    pyautogui.hotkey('tab')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar em SALVAR ATIVIDADE
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    pyautogui.sleep(0.3)

    # Clicar na aba ASSOCIAÇÕES
    pyautogui.click(810, 294)

    # Clicar no campo Administração Regional do Técnico Senar Responsável
    pyautogui.hotkey('tab')
    # Pressionar Ctrl + A para selecionar todo o texto
    pyautogui.hotkey('ctrl', 'a')
    # Pressionar Delete para apagar o texto selecionado
    keyboard.write('Goiás')
    pyautogui.sleep(0.3)

    # Clicar no campo Sindicato Rural Associado
    pyautogui.hotkey('tab')
    # Pressionar Ctrl + A para selecionar todo o texto
    pyautogui.hotkey('ctrl', 'a')
    # Pressionar Delete para apagar o texto selecionado
    keyboard.write('Itaberaí')

    # Clicar no campo Associação a cooperativa
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    # Pressionar Ctrl + A para selecionar todo o texto
    pyautogui.hotkey('ctrl', 'a')
    # Pressionar Delete para apagar o texto selecionado
    keyboard.write('Não possui')

    # Clicar em SALVAR ATIVIDADE
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')

    # Clicar na aba Informações Adicionais
    pyautogui.click(939, 299)

    # Clicar no campo Estado Civil
    pyautogui.hotkey('tab')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')

    # Clicar na opção Sucessão Familiar
    pyautogui.hotkey('tab')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')

    # Clicar no botão Salvar Informações Adicionais
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')


print("Função personalizada foi chamada!")
# Adicione qualquer lógica adicional conforme necessário

#dados_solicitante()

# Tirar hashtag se quiser reproduzir somente esse script