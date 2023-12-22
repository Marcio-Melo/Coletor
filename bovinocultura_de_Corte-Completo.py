from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time

# - Preenchimento da aba Bovinocultura de leite:
# Atividade Rural
# Condomínio Agropecuário

"""# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.5)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(0.5)

# Clicar botão Preencher ano (2020)
pyautogui.click(1631, 208, duration=0.5)"""

# Ir para outra tela
pyautogui.click(649,874)

# ir para campo Ciclo Produtivo
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Completo)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.5)

# ir para campo Sistema de Produção
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Extensivo), (Semi Intensivo) e (Intensivo/Confinamento) - não mudam nada
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down') # Semi Intensivo
pyautogui.hotkey('down') # Intensivo/Confinamento)
pyautogui.press('enter')
pyautogui.sleep(0.5)

# ir para o campo Área da propriedade - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('7000')

# ir para o campo Área da Propriedade - Arrendada(ha)
pyautogui.hotkey('tab')
# Digitar valor
pyautogui.sleep(0.5)
keyboard.write('6000')

# ir para o campo Área para Pecuária - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('7000')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)

# ir para o campo Área para Pecuária - Arrendada(ha)
# Digitar valor
keyboard.write('6000')
pyautogui.hotkey('tab')

# ir para o campo Área para Produção de Forrageiras - Própria(ha)
# Digitar valor
pyautogui.sleep(0.5)
keyboard.write('7000')

# ir para o campo Área para Produção de Forrageiras - Arrendada(ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('6000')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)

# Aguarde um curto período
pyautogui.sleep(0.5)
# clicar no botão prosseguir
pyautogui.hotkey('enter')
pyautogui.sleep(5)

# TELA Fêmeas
# Vacas (Matrizes)

# ir para campo Quantidade (cab/ano)
pyautogui.moveTo(831,480)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50')

# ir para Peso médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('400')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto perío10  do
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('300')

# Fêmeas em Aleitamento

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('45')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('400')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5400')

# Fêmeas em Recria

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('100')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('100 0')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('500')

# Fêmeas em Terminação

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('1800')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5000')

# Ir para botão prosseguir
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Clicar no botão Prosseguir
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Touros (Reprodudores)

# ir para campo Quantidade (cab/ano)
pyautogui.moveTo(161,934)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50')
pyautogui.sleep(0.5)

# ir para Peso médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('400')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('300')

# Machos em Aleitamento

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('500')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5000')

# Machos em Recria

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('500')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('500')

# Machos em Terminação

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('200')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('2000')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5000')

# Ir para botão prosseguir
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Clicar no botão Prosseguir
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Produção

# Ir para campo Produtividade (@/ha/ano)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5000')

# Ir para campo Preço médio da @ (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5000')

# Ir para campo Custo mensal (R$/cab/ano) *média do ano
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5000')

# Ir para campo Taxa de Lotação (UA/ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('4000')

# Ir para campo Ganho de peso diário (Kg/dia)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5000')

# Finanças

# Ir para campo Custo Total (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5000')

# Ir para campo Custo Operacional Total (R$/ano)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5000')

# Ir para campo Custo Operacional Efetivo (R$/ano)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5000')

# Inventário animal
# Ir para campo Valor Total do Inventário Animal (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5000')

# Ir para botão Prosseguir
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Confinamento
# Ir para campo Capacidade estática de lotação do Confinamento (Cabeças)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5000')

# Ir para campo Dias de Confinamento
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5000')

# Ir para campo Diária Confinamento (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5000')

# Índices Zootécnicos
# Ir para campo Taxa de Descarte - Fêmeas (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5000')

# Ir para campo Taxa de Desfrute - Rebanho (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5000')

# Ir para campo Taxa de Desmame - Rebanho (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5000')

# Ir para botão Concluir
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
