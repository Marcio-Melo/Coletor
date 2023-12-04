from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time

pyautogui.PAUSE = 0.3
# Rolar para baixo imediatamente
# Este comando depende do sistema operacional (Ctrl + seta para baixo)
pyautogui.click(1616, 320, duration=0.3)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
#pyautogui.sleep(2)

# Clicar no campo RG e preencher
pyautogui.click(1014, 519, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
pyautogui.write('4226134')

# Clicar no campo Orgão/UF e Preencher
pyautogui.click(1548, 516, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
pyautogui.write('DGPC GO')

# Clicar no campo Data de Emissão e preencher
pyautogui.click(680, 630, duration=0.3)

# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
pyautogui.write('12/09/1999')

# Clicar no campo Nacionalidade e preencher
pyautogui.click(1051, 630, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
pyautogui.write('Brasileiro')

# Clicar no campo Naturalidade e preencher
pyautogui.click(1431, 620, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Escrever a palavra com acento usando a biblioteca keyboard
keyboard.write('Goiás')

# Clicar no campo Telefone e preencher
pyautogui.click(793, 740, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
pyautogui.write('(62) 99982-1750')

# Clicar no campo E-mail e preencher
pyautogui.click(1189, 748, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
pyautogui.write('miguelzinhobaiano@gmail.com')

# Clicar no campo Data de Nascimento e preencher
pyautogui.click(1542, 739, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
pyautogui.write('09/06/1982')

# Clicar no botão Salvar Informações Gerais
pyautogui.click(1640, 848, duration=0.3)


# ABA ENDEREÇO
# Clicar na aba ENDEREÇO
pyautogui.click(748, 305, duration=0.3)

# Clicar no campo CEP
pyautogui.click(665, 406, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
pyautogui.write('76630-000')

# Clicar no campo UF
pyautogui.click(1132, 402, duration=0.3)

# Clicar na UF GO
pyautogui.click(1121, 835, duration=0.3)

# Clicar no campo Município
pyautogui.click(1551, 402, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
keyboard.write('Itaberai')
pyautogui.click(1540, 449, duration=0.3)

# Clicar no campo ENDEREÇO
pyautogui.click(776, 514, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('Rua Luiz Antonio - QD 26 LT 32 - Centro')

# Clicar no campo BAIRRO
pyautogui.click(1472, 521, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('não tem')

# Clicar no campo NÚMERO
pyautogui.click(628, 640, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('não tem')

# Clicar no campo COMPLEMENTO
pyautogui.click(1121, 641, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('não tem')

# Clicar no campo TEMPO DE RESIDÊNCIA NO MUNICÍPIO
pyautogui.click(1535, 631, duration=0.3)
# Clicar na opção 10 a 15 anos
pyautogui.click(1543, 829, duration=0.3)

# Clicar em SALVAR ENDEREÇO
pyautogui.click(1754, 733, duration=0.3)

# Clicar na aba ATIVIDADE
pyautogui.click(857, 300, duration=0.3)

# Clicar no campo Nome da Propriedade
pyautogui.click(767, 403, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('Fazenda Bom Futura')


# Clicar no campo TEMPO DE EXERCÍCIO NESSA ATIVIDADE (ANOS)
pyautogui.click(1053, 532, duration=0.3)
# Clicar na opção Até 2 anos
pyautogui.click(1074, 559, duration=0.3)

# Clicar no campo PRINCIPAL UF DE ATUAÇÃO
pyautogui.click(1497, 517, duration=0.3)
# Clicar na opção PR
pyautogui.click(1446, 465, duration=0.3)

# Clicar no campo Principal Município de Atuação
pyautogui.click(701, 632, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
keyboard.write('Alexania')
pyautogui.click(697, 672, duration=0.3)

# Clicar no campo Perfil do Produtor
pyautogui.click(1136, 629, duration=0.3)
# Clicar na opção PR
pyautogui.click(1126, 673, duration=0.3)

# Clicar em SALVAR ATIVIDADE
pyautogui.click(1684, 739, duration=0.3)

# Clicar na aba ASSOCIAÇÕES
pyautogui.click(961, 306, duration=0.3)
# Clicar no campo Administração Regional do Técnico Senar Responsável
pyautogui.click(1500, 394, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
keyboard.write('Goiás')

# Clicar no campo Sindicato Rural Associado
pyautogui.click(736, 517, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
keyboard.write('Itaberaí')

# Clicar no campo Associação a cooperativa
pyautogui.click(1357, 520, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
keyboard.write('Não possui')

# Clicar em SALVAR ATIVIDADE
pyautogui.click(1743, 653, duration=0.3)

# Clicar na aba Informações Adicionais
pyautogui.click(1152, 297, duration=0.3)

# Clicar no campo Estado Civil
pyautogui.click(684, 406, duration=0.3)

# Clicar na opção Solteiro
pyautogui.click(718, 445, duration=0.3)

# Clicar na opção Sucessão Familiar
pyautogui.click(1096, 400, duration=0.3)

# Clicar na opção Sim
pyautogui.click(1223, 447, duration=0.3)

# Clicar no botão Salvar Informações Adicionais
pyautogui.click(1643, 512, duration=0.3)

'''
# CMD
# Python
# from mouseinfo import mouseInfo
# mouseInfo()
# desmarcar 3 sec delay
'''