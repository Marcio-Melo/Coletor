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

# Aguarde um curto período
pyautogui.sleep(0.5)

# Clicar botão Preencher ano (2022)
pyautogui.click(1630,384, duration=0.5)

# ir para campo Sistema de Produção
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Extensivo)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.5)

# ir para campo Sistema de Ordenha
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Mecânico)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.5)

# ir para campo Tipo de Atividade Leiteira
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Produção de leite)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')

# Aguarde um curto período
pyautogui.sleep(0.5)
# ir para o campo Área da propriedade - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)

# Digitar valor
keyboard.write('7000')
pyautogui.hotkey('tab')

# Aguarde um curto período
# ir para o campo Área da Propriedade - Arrendada(ha)
# Digitar valor
pyautogui.sleep(0.5)
keyboard.write('6000')

# ir para o campo Área Produtiva - Própria(ha)
# Digitar valor
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
keyboard.write('7000')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)

# ir para o campo Área Produtiva - Arrendada(ha)
# Digitar valor
keyboard.write('6000')
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# clicar no botão prosseguir
pyautogui.hotkey('enter')

# TELA REBANHO
# ir para campo Vacas (Lactação)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50')

# ir para campo Vacas (Secas)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50')

# ir para campo Fêmeas 0-12 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('20')

# ir para campo Fêmeas 13-24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('30')

# ir para campo Fêmeas 25-36 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('45')

# ir para campo Fêmeas +36 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('45')

# MACHOS
# ir para campo Reprodutores
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5454')

# ir para campo RUFIÕES
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('10')

# ir para campo Machos 0-12 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('487')

# ir para campo Machos 13-24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('345')

# ir para campo Machos +24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('129')

# ir para botão PROSSEGUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Clicar em enter
# ir para botão PROSSEGUIR
pyautogui.hotkey('enter')

# Aba PRODUÇÃO DE LEITE
# ir para campo Vacas em Lactação (Cab/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('300')

# ir para campo Produtividade (l/vaca/dia)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('60')

# ir para campo Leite para Consumo (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('4545')

# ir para campo Leite para Descarte (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5644')

# ir para campo Leite para Aleitamento (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('129')

# ir para campo Média de Preço de Venda do Leite (R$/l)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('129')

# ir para campo CCS (Células/mL)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('129')

# ir para campo CBT (UFC/mL)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('129')

# ir para campo Média de Bonificação no Preço do Leite (R$/l)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('129')

# ir para BOTÃO PROSSEGUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# clicar no BOTÃO PROSSEGUIR
pyautogui.hotkey('enter')

# Aguarde um curto período
pyautogui.sleep(0.5)

# ABA COMERCIALIZAÇÃO
# ir para campo Custo Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('7897898')

# ir para campo Custo Operacional Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('5464544')

# ir para campo Custo Operacional Efetivo Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('2312312')

# ir para BOTÃO CONCLUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.5)

# clicar no BOTÃO CONCLUIR
pyautogui.hotkey('enter')