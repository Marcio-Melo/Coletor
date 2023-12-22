from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time


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
# Selecionar opção (Cria)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
        
pyautogui.press('enter')
pyautogui.sleep(0.5)

# ir para campo Sistema de Produção
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Extensivo)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.5)

# ir para o campo Área da Propriedade - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('7001')

# ir para o campo Área da Propriedade - Arrendada(ha)
pyautogui.hotkey('tab')
# Digitar valor
pyautogui.sleep(0.5)
keyboard.write('6001')

# ir para o campo Área para Pecuária - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('7001')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)

# ir para o campo Área para Pecuária - Arrendada(ha)
# Digitar valor
keyboard.write('6001')
pyautogui.hotkey('tab')

# ir para o campo Área para Produção de Forrageiras - Própria(ha)
# Digitar valor
pyautogui.sleep(0.5)
keyboard.write('7001')

# ir para o campo Área para Produção de Forrageiras - Arrendada(ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('6001')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)

# Aguarde um curto período
pyautogui.sleep(0.5)
# clicar no botão prosseguir
pyautogui.hotkey('enter')

# TELA Fêmeas
# Vacas (Matrizes)

# ir para campo Quantidade (cab/ano)
pyautogui.moveTo(161, 934)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto perío10  do
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Fêmeas em Aleitamento

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('4')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Fêmeas em Recria

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Fêmeas em Terminação

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para botão prosseguir
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Clicar no botão Prosseguir
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Touros (Reprodudores)

# ir para campo Quantidade (cab/ano)
pyautogui.moveTo(161, 934)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')
pyautogui.sleep(0.5)

# ir para Peso médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Machos em Aleitamento

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('4')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Machos em Recria

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Machos em Terminação

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

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
keyboard.write('50,1')

# Ir para campo Preço médio da @ (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Custo mensal (R$/cab/ano) *média do ano
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Taxa de Lotação (UA/ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Ganho de peso diário (Kg/dia)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Finanças

# Ir para campo Custo Total (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Custo Operacional Total (R$/ano)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Custo Operacional Efetivo (R$/ano)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Inventário animal
# Ir para campo Valor Total do Inventário Animal (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

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
keyboard.write('50,1')

# Ir para campo Dias de Confinamento
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Diária Confinamento (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Índices Zootécnicos
# Ir para campo Taxa de Descarte - Fêmeas (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Taxa de Desfrute - Rebanho (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Taxa de Desmame - Rebanho (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para botão Concluir
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.5)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(0.5)

# Clicar botão Preencher ano (2021)
pyautogui.click(1624, 296, duration=0.5)

# ir para campo Ciclo Produtivo
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Cria)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.5)
# ir para o campo Área da Propriedade - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('7001')

# ir para o campo Área da Propriedade - Arrendada(ha)
pyautogui.hotkey('tab')
# Digitar valor
pyautogui.sleep(0.5)
keyboard.write('6001')

# ir para o campo Área para Pecuária - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('7001')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)

# ir para o campo Área para Pecuária - Arrendada(ha)
# Digitar valor
keyboard.write('6001')
pyautogui.hotkey('tab')

# ir para o campo Área para Produção de Forrageiras - Própria(ha)
# Digitar valor
pyautogui.sleep(0.5)
keyboard.write('7001')

# ir para o campo Área para Produção de Forrageiras - Arrendada(ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('6001')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)

# Aguarde um curto período
pyautogui.sleep(0.5)
# clicar no botão prosseguir
pyautogui.hotkey('enter')

# TELA Fêmeas
# Vacas (Matrizes)

# ir para campo Quantidade (cab/ano)
pyautogui.moveTo(161, 934)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto perío10  do
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Fêmeas em Aleitamento

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('4')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Fêmeas em Recria

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Fêmeas em Terminação

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para botão prosseguir
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Clicar no botão Prosseguir
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Touros (Reprodudores)

# ir para campo Quantidade (cab/ano)
pyautogui.moveTo(161, 934)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')
pyautogui.sleep(0.5)

# ir para Peso médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Machos em Aleitamento

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('4')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Machos em Recria

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Machos em Terminação

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

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
keyboard.write('50,1')

# Ir para campo Preço médio da @ (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Custo mensal (R$/cab/ano) *média do ano
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Taxa de Lotação (UA/ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Ganho de peso diário (Kg/dia)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Finanças

# Ir para campo Custo Total (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Custo Operacional Total (R$/ano)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Custo Operacional Efetivo (R$/ano)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Inventário animal
# Ir para campo Valor Total do Inventário Animal (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

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
keyboard.write('50,1')

# Ir para campo Dias de Confinamento
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Diária Confinamento (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Índices Zootécnicos
# Ir para campo Taxa de Descarte - Fêmeas (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Taxa de Desfrute - Rebanho (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Taxa de Desmame - Rebanho (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para botão Concluir
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.5)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(0.5)

# Clicar botão Preencher ano (2022)
pyautogui.click(1628, 390, duration=0.5)

# ir para campo Ciclo Produtivo
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Cria)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.5)

# ir para o campo Área da Propriedade - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('7001')

# ir para o campo Área da Propriedade - Arrendada(ha)
pyautogui.hotkey('tab')
# Digitar valor
pyautogui.sleep(0.5)
keyboard.write('6001')

# ir para o campo Área para Pecuária - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('7001')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)

# ir para o campo Área para Pecuária - Arrendada(ha)
# Digitar valor
keyboard.write('6001')
pyautogui.hotkey('tab')

# ir para o campo Área para Produção de Forrageiras - Própria(ha)
# Digitar valor
pyautogui.sleep(0.5)
keyboard.write('7001')

# ir para o campo Área para Produção de Forrageiras - Arrendada(ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('6001')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)

# Aguarde um curto período
pyautogui.sleep(0.5)
# clicar no botão prosseguir
pyautogui.hotkey('enter')

# TELA Fêmeas
# Vacas (Matrizes)

# ir para campo Quantidade (cab/ano)
pyautogui.moveTo(161, 934)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto perío10  do
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Fêmeas em Aleitamento

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('4')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Fêmeas em Recria

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Fêmeas em Terminação

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para botão prosseguir
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Clicar no botão Prosseguir
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Touros (Reprodudores)

# ir para campo Quantidade (cab/ano)
pyautogui.moveTo(161, 934)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')
pyautogui.sleep(0.5)

# ir para Peso médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Machos em Aleitamento

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('4')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Machos em Recria

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Machos em Terminação

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

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
keyboard.write('50,1')

# Ir para campo Preço médio da @ (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Custo mensal (R$/cab/ano) *média do ano
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Taxa de Lotação (UA/ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Ganho de peso diário (Kg/dia)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Finanças

# Ir para campo Custo Total (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Custo Operacional Total (R$/ano)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Custo Operacional Efetivo (R$/ano)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Inventário animal
# Ir para campo Valor Total do Inventário Animal (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

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
keyboard.write('50,1')

# Ir para campo Dias de Confinamento
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Diária Confinamento (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Índices Zootécnicos
# Ir para campo Taxa de Descarte - Fêmeas (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Taxa de Desfrute - Rebanho (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Taxa de Desmame - Rebanho (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para botão Concluir
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.5)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(0.5)

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.5)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(0.5)

# Clicar botão Preencher ano (2023)
pyautogui.click(1641, 470, duration=0.5)

# ir para o campo Área da Propriedade - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('7001')

# ir para o campo Área da Propriedade - Arrendada(ha)
pyautogui.hotkey('tab')
# Digitar valor
pyautogui.sleep(0.5)
keyboard.write('6001')

# ir para o campo Área para Pecuária - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('7001')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)

# ir para o campo Área para Pecuária - Arrendada(ha)
# Digitar valor
keyboard.write('6001')
pyautogui.hotkey('tab')

# ir para o campo Área para Produção de Forrageiras - Própria(ha)
# Digitar valor
pyautogui.sleep(0.5)
keyboard.write('7001')

# ir para o campo Área para Produção de Forrageiras - Arrendada(ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('6001')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)

# Aguarde um curto período
pyautogui.sleep(0.5)
# clicar no botão prosseguir
pyautogui.hotkey('enter')

# TELA Fêmeas
# Vacas (Matrizes)

# ir para campo Quantidade (cab/ano)
pyautogui.moveTo(161, 934)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto perío10  do
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Fêmeas em Aleitamento

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('4')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Fêmeas em Recria

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Fêmeas em Terminação

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para botão prosseguir
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Clicar no botão Prosseguir
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Touros (Reprodudores)

# ir para campo Quantidade (cab/ano)
pyautogui.moveTo(161, 934)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')
pyautogui.sleep(0.5)

# ir para Peso médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Machos em Aleitamento

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('4')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Machos em Recria

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Machos em Terminação

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

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
keyboard.write('50,1')

# Ir para campo Preço médio da @ (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Custo mensal (R$/cab/ano) *média do ano
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Taxa de Lotação (UA/ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Ganho de peso diário (Kg/dia)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Finanças

# Ir para campo Custo Total (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Custo Operacional Total (R$/ano)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Custo Operacional Efetivo (R$/ano)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Inventário animal
# Ir para campo Valor Total do Inventário Animal (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

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
keyboard.write('50,1')

# Ir para campo Dias de Confinamento
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Diária Confinamento (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Índices Zootécnicos
# Ir para campo Taxa de Descarte - Fêmeas (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Taxa de Desfrute - Rebanho (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Taxa de Desmame - Rebanho (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para botão Concluir
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.5)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(0.5)

# Clicar botão Preencher ano (2024)
pyautogui.click(1655, 556, duration=0.5)

# ir para o campo Área da Propriedade - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('7001')

# ir para o campo Área da Propriedade - Arrendada(ha)
pyautogui.hotkey('tab')
# Digitar valor
pyautogui.sleep(0.5)
keyboard.write('6001')

# ir para o campo Área para Pecuária - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('7001')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)

# ir para o campo Área para Pecuária - Arrendada(ha)
# Digitar valor
keyboard.write('6001')
pyautogui.hotkey('tab')

# ir para o campo Área para Produção de Forrageiras - Própria(ha)
# Digitar valor
pyautogui.sleep(0.5)
keyboard.write('7001')

# ir para o campo Área para Produção de Forrageiras - Arrendada(ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('6001')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)

# Aguarde um curto período
pyautogui.sleep(0.5)
# clicar no botão prosseguir
pyautogui.hotkey('enter')

# TELA Fêmeas
# Vacas (Matrizes)

# ir para campo Quantidade (cab/ano)
pyautogui.moveTo(161, 934)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto perío10  do
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Fêmeas em Aleitamento

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('4')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Fêmeas em Recria

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Fêmeas em Terminação

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para botão prosseguir
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Clicar no botão Prosseguir
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Touros (Reprodudores)

# ir para campo Quantidade (cab/ano)
pyautogui.moveTo(161, 934)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')
pyautogui.sleep(0.5)

# ir para Peso médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Machos em Aleitamento

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('4')

# ir para Preço médio de venda (R$/@/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Machos em Recria

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Machos em Terminação

# ir para Quantidade (cab/ano)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# ir para Peso médio de venda (@)
pyautogui.hotkey('tab')
# Aguarde um curto período
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

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
keyboard.write('50,1')

# Ir para campo Preço médio da @ (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Custo mensal (R$/cab/ano) *média do ano
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Taxa de Lotação (UA/ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Ganho de peso diário (Kg/dia)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Finanças

# Ir para campo Custo Total (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Custo Operacional Total (R$/ano)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Custo Operacional Efetivo (R$/ano)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Inventário animal
# Ir para campo Valor Total do Inventário Animal (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

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
keyboard.write('50,1')

# Ir para campo Dias de Confinamento
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Diária Confinamento (R$)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Índices Zootécnicos
# Ir para campo Taxa de Descarte - Fêmeas (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Taxa de Desfrute - Rebanho (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para campo Taxa de Desmame - Rebanho (%)
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# Digitar valor
keyboard.write('50,1')

# Ir para botão Concluir
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.5)
pyautogui.hotkey('ctrl', 'end')

# Clicar em propriedade rurais
pyautogui.click(243,443, duration=0.5)

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.5)
pyautogui.hotkey('ctrl', 'end')

# clicar no botão Adicionar Propriedade
pyautogui.click(1695,257, duration=0.5)

# clicar na combo Tipo da propriedade
pyautogui.click(1545,243, duration=0.5)

# selecionar Própria
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.3)

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

# Ir para o campo Arrendatário
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para Arrendatário
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

# Ir para o campo Início Arrendamento
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor Início Arrendamento
keyboard.write('12122023')
pyautogui.sleep(0.5)

# Ir para o campo Término Arrendamento
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor Término Arrendamento
keyboard.write('27122023')
pyautogui.sleep(0.5)

# Ir para o campo Área Arrendada
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para Área Arrendada
keyboard.write('85645')
pyautogui.sleep(0.5)

# Ir para o campo Atividade Principal
pyautogui.hotkey('tab')
# preencher valor para Atividade Principal (cultivo de algodão)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)

# Ir para o campo Valor Total do Arrendamento (R$/ano)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.5)
# preencher valor para Valor Total do Arrendamento (R$/ano)
keyboard.write('85645')
pyautogui.sleep(0.5)

# Clicar no botão Salvar Propriedade
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
pyautogui.sleep(0.5)