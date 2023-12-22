from os.path import realpath, dirname
import pyautogui
import keyboard
import random
import pytest
import time

# - Preenchimento da tela inicial e página de login
# INFORMAÇÕES GERAIS

# Clicar em pular
pyautogui.click(1726, 902, duration=0.3)

# Clicar e digitar meu usuário
pyautogui.click(1557, 555, duration=0.3)
pyautogui.write('marcio')

# Clicar e digitar minha senha
pyautogui.click(1383, 664, duration=0.3)
pyautogui.write('marcio')

# Clicar no botão lembrar-me
pyautogui.click(1270, 731, duration=0.3)

# Clicar em entrar
pyautogui.click(1333, 802, duration=0.3)

# Rolar para baixo imediatamente
# Este comando depende do sistema operacional (Ctrl + seta para baixo)
pyautogui.click(1616, 320, duration=0.3)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(1)

# Clicar em Nova operação
pyautogui.click(1638, 291, duration=0.3)

# Clicar na combo Solicitante
pyautogui.sleep(1)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(1)
pyautogui.hotkey('down')
# Seleciona Cosme Moraes
pyautogui.hotkey('down')
pyautogui.sleep(1)

# Seleciona Ronilson Moraes
pyautogui.hotkey('down')
# pyautogui.sleep(1)

# Seleciona José Damião
# pyautogui.hotkey('down')
# pyautogui.sleep(1)

# Selecionar Solicitante
pyautogui.hotkey('enter')
# Atividade Principal já setada (Bovinocultura de leite)

# Clicar em Iniciar Operação
pyautogui.click(1548, 630, duration=0.3)

# Clicar em Iniciar Operação
pyautogui.click(1548, 630, duration=0.3)

# Rolar para baixo imediatamente
# Este comando depende do sistema operacional (Ctrl + seta para baixo)
pyautogui.click(1616, 320, duration=0.3)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(1)

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

# Clicar na aba Crédito
pyautogui.click(280, 373, duration=0.3)

# - Preenchimento da aba Crédito:
# Crédito

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.3)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(1)

# Clicar no campo Valor solicitado
pyautogui.click(711, 357, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
pyautogui.write('21220311')

# Clicar no campo Descreva o detalhamento sobra a finalidade
pyautogui.click(761, 465, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write(
    'Aquisição de matrizes e compra de insumos para produção de forrageiras.')

# Clicar no botão Salvar Crédito
pyautogui.click(1704, 667, duration=0.3)

# Clicar na atividade rural
pyautogui.click(230, 427, duration=0.3)

# - Preenchimento da aba ATIVIDADE RURAL:
# Atividade Rural
# Condomínio Agropecuário

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.3)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(1)

# Clicar no campo Nome do Grupo
pyautogui.click(766, 477, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('João Miguel da Silva')

# Clicar no campo Percentual societário do solicitante
pyautogui.click(1283, 472, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('9999')

# Outros participantes da atividade
# Clicar no campo Nome Completo
pyautogui.click(777, 683, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('Outra pessoa')

# Clicar no campo CPF / CNPJ
pyautogui.click(1078, 688, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('03966695146')

# Clicar no campo % Societário
pyautogui.click(1491, 685, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('1')

# Clicar no botão Salvar Condomínio
pyautogui.click(1672, 852, duration=0.3)

# Clicar na Aba Principais Fornecedores
pyautogui.click(837, 307, duration=0.3)

# Clicar no campo Nome do Fornecedor
pyautogui.click(732, 491, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('Sementes Plante')

# Clicar no campo Prazo Médio de Compras
pyautogui.click(1118, 496, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
# Pressionar Delete para apagar o texto selecionado
pyautogui.click(1213, 533, duration=0.3)

# Clicar no campo % Participação
pyautogui.click(1431, 494, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('10000')

# Clicar no botão Salvar Principais Fornecedores
pyautogui.click(1657, 643, duration=0.3)

# Clicar na Principais Clientes
pyautogui.click(1049, 306, duration=0.3)

# Clicar no campo Nome do Cliente
pyautogui.click(757, 499, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('São Salvador Alimentos')

# Botão com comportamento diferente (não aceita usar "Tab")
# Clicar no campo Prazo Médio de Compras
pyautogui.click(1118, 496, duration=0.3)
# Clicar em Semestral
pyautogui.click(1213, 533, duration=0.3)

# Clicar no campo % Participação
pyautogui.click(1431, 494, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('10000')

# Clicar no botão SALVAR PRINCIPAIS CLIENTES
pyautogui.click(1677, 638, duration=0.3)

# Clicar na aba SEGURO RURAL
pyautogui.click(1211, 302, duration=0.3)

# Clicar no campo Seguro Rural
pyautogui.click(794, 497, duration=0.3)
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
pyautogui.click(1355, 307, duration=0.3)

# Clicar no campo Selos e Certificações
pyautogui.click(815, 502, duration=0.3)
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
pyautogui.click(1530, 300, duration=0.3)

# Clicar no campo Iniciativas Socioambientais
pyautogui.click(815, 502, duration=0.3)
# Pressionar Ctrl + A para selecionar todo o texto
pyautogui.hotkey('ctrl', 'a')
# Pressionar Delete para apagar o texto selecionado
keyboard.write('Energia')

pyautogui.hotkey('tab')
# ir para o botão salvar Iniciativas Socioambientais
pyautogui.hotkey('tab')
# Realizar o clique após a tecla "Tab"
pyautogui.hotkey('enter')

# Clicar na aba Bovinocultura
pyautogui.click(263, 498, duration=0.3)

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.3)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(0.3)

# Clicar botão Preencher ano (2020)
pyautogui.click(1631, 208, duration=0.3)

# ir para campo Sistema de Produção
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Extensivo)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.3)

# ir para campo Sistema de Ordenha
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Mecânico)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.3)

# ir para campo Tipo de Atividade Leiteira
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Produção de leite)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')

# Aguarde um curto período
pyautogui.sleep(0.3)
# ir para o campo Área da propriedade - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

# Digitar valor
keyboard.write('7000')
pyautogui.hotkey('tab')

# Aguarde um curto período
# ir para o campo Área da Propriedade - Arrendada(ha)
# Digitar valor
pyautogui.sleep(0.3)
keyboard.write('6000')

# ir para o campo Área Produtiva - Própria(ha)
# Digitar valor
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
keyboard.write('7000')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

# ir para o campo Área Produtiva - Arrendada(ha)
# Digitar valor
keyboard.write('6000')
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# clicar no botão prosseguir
pyautogui.hotkey('enter')

# TELA REBANHO
# ir para campo Vacas (Lactação)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('50')

# ir para campo Vacas (Secas)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('50')

# ir para campo Fêmeas 0-12 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('20')

# ir para campo Fêmeas 13-24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('30')

# ir para campo Fêmeas 25-36 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('45')

# ir para campo Fêmeas +36 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('45')

# MACHOS
# ir para campo Reprodutores
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('5454')

# ir para campo RUFIÕES
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('10')

# ir para campo Machos 0-12 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('487')

# ir para campo Machos 13-24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('345')

# ir para campo Machos +24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para botão PROSSEGUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Clicar em enter
# ir para botão PROSSEGUIR
pyautogui.hotkey('enter')

# Aba PRODUÇÃO DE LEITE
# ir para campo Vacas em Lactação (Cab/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('300')

# ir para campo Produtividade (l/vaca/dia)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('6000')

# ir para campo Leite para Consumo (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('4545')

# ir para campo Leite para Descarte (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('5644')

# ir para campo Leite para Aleitamento (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para campo Média de Preço de Venda do Leite (R$/l)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('399')

# ir para campo CCS (Células/mL)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para campo CBT (UFC/mL)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para campo Média de Bonificação no Preço do Leite (R$/l)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para BOTÃO PROSSEGUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# clicar no BOTÃO PROSSEGUIR
pyautogui.hotkey('enter')

# Aguarde um curto período
pyautogui.sleep(0.3)

# ABA COMERCIALIZAÇÃO
# ir para campo Custo Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('7897898')

# ir para campo Custo Operacional Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('5464544')

# ir para campo Custo Operacional Efetivo Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('2312312')

# ir para BOTÃO CONCLUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)

# clicar no BOTÃO CONCLUIR
pyautogui.hotkey('enter')

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.3)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(0.3)

# Clicar botão Preencher ano (2021)
pyautogui.click(1649, 289, duration=0.3)

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.3)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(0.3)

# Clicar botão Preencher ano (2020)
pyautogui.click(1631, 208, duration=0.3)

# ir para campo Sistema de Produção
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Extensivo)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.3)

# ir para campo Sistema de Ordenha
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Mecânico)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.3)

# ir para campo Tipo de Atividade Leiteira
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Produção de leite)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')

# Aguarde um curto período
pyautogui.sleep(0.3)
# ir para o campo Área da propriedade - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

# Digitar valor
keyboard.write('7000')
pyautogui.hotkey('tab')

# Aguarde um curto período
# ir para o campo Área da Propriedade - Arrendada(ha)
# Digitar valor
pyautogui.sleep(0.3)
keyboard.write('6000')

# ir para o campo Área Produtiva - Própria(ha)
# Digitar valor
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
keyboard.write('7000')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

# ir para o campo Área Produtiva - Arrendada(ha)
# Digitar valor
keyboard.write('6000')
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# clicar no botão prosseguir
pyautogui.hotkey('enter')

# TELA REBANHO
# ir para campo Vacas (Lactação)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('50')

# ir para campo Vacas (Secas)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('50')

# ir para campo Fêmeas 0-12 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('20')

# ir para campo Fêmeas 13-24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('30')

# ir para campo Fêmeas 25-36 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('45')

# ir para campo Fêmeas +36 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('45')

# MACHOS
# ir para campo Reprodutores
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('5454')

# ir para campo RUFIÕES
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('10')

# ir para campo Machos 0-12 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('487')

# ir para campo Machos 13-24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('345')

# ir para campo Machos +24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para botão PROSSEGUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Clicar em enter
# ir para botão PROSSEGUIR
pyautogui.hotkey('enter')

# Aba PRODUÇÃO DE LEITE
# ir para campo Vacas em Lactação (Cab/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('300')

# ir para campo Produtividade (l/vaca/dia)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('6000')

# ir para campo Leite para Consumo (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('4545')

# ir para campo Leite para Descarte (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('5644')

# ir para campo Leite para Aleitamento (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para campo Média de Preço de Venda do Leite (R$/l)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('399')

# ir para campo CCS (Células/mL)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para campo CBT (UFC/mL)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para campo Média de Bonificação no Preço do Leite (R$/l)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('199')

# ir para BOTÃO PROSSEGUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# clicar no BOTÃO PROSSEGUIR
pyautogui.hotkey('enter')

# Aguarde um curto período
pyautogui.sleep(0.3)

# ABA COMERCIALIZAÇÃO
# ir para campo Custo Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('7897898')

# ir para campo Custo Operacional Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('5464544')

# ir para campo Custo Operacional Efetivo Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('2312312')

# ir para BOTÃO CONCLUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)

# clicar no BOTÃO CONCLUIR
pyautogui.hotkey('enter')

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.3)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(0.3)

# Clicar botão Preencher ano (2022)
pyautogui.click(1630, 384, duration=0.3)

# ir para campo Sistema de Produção
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Extensivo)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.3)

# ir para campo Sistema de Ordenha
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Mecânico)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.3)

# ir para campo Tipo de Atividade Leiteira
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Produção de leite)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')

# Aguarde um curto período
pyautogui.sleep(0.3)
# ir para o campo Área da propriedade - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

# Digitar valor
keyboard.write('7000')
pyautogui.hotkey('tab')

# Aguarde um curto período
# ir para o campo Área da Propriedade - Arrendada(ha)
# Digitar valor
pyautogui.sleep(0.3)
keyboard.write('6000')

# ir para o campo Área Produtiva - Própria(ha)
# Digitar valor
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
keyboard.write('7000')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

# ir para o campo Área Produtiva - Arrendada(ha)
# Digitar valor
keyboard.write('6000')
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# clicar no botão prosseguir
pyautogui.hotkey('enter')

# TELA REBANHO
# ir para campo Vacas (Lactação)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('50')

# ir para campo Vacas (Secas)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('50')

# ir para campo Fêmeas 0-12 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('20')

# ir para campo Fêmeas 13-24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('30')

# ir para campo Fêmeas 25-36 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('45')

# ir para campo Fêmeas +36 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('45')

# MACHOS
# ir para campo Reprodutores
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('5454')

# ir para campo RUFIÕES
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('10')

# ir para campo Machos 0-12 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('487')

# ir para campo Machos 13-24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('345')

# ir para campo Machos +24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para botão PROSSEGUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Clicar em enter
# ir para botão PROSSEGUIR
pyautogui.hotkey('enter')

# Aba PRODUÇÃO DE LEITE
# ir para campo Vacas em Lactação (Cab/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('300')

# ir para campo Produtividade (l/vaca/dia)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('6000')

# ir para campo Leite para Consumo (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('4545')

# ir para campo Leite para Descarte (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('5644')

# ir para campo Leite para Aleitamento (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para campo Média de Preço de Venda do Leite (R$/l)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('399')

# ir para campo CCS (Células/mL)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para campo CBT (UFC/mL)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para campo Média de Bonificação no Preço do Leite (R$/l)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para BOTÃO PROSSEGUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# clicar no BOTÃO PROSSEGUIR
pyautogui.hotkey('enter')

# Aguarde um curto período
pyautogui.sleep(0.3)

# ABA COMERCIALIZAÇÃO
# ir para campo Custo Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('7897898')

# ir para campo Custo Operacional Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('5464544')

# ir para campo Custo Operacional Efetivo Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('2312312')

# ir para BOTÃO CONCLUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)

# clicar no BOTÃO CONCLUIR
pyautogui.hotkey('enter')

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.3)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(0.3)

# Clicar botão Preencher ano (2023)
pyautogui.click(1657, 468, duration=0.3)

# ir para campo Sistema de Produção
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Extensivo)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.3)

# ir para campo Sistema de Ordenha
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Mecânico)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.3)

# ir para campo Tipo de Atividade Leiteira
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Produção de leite)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')

# Aguarde um curto período
pyautogui.sleep(0.3)
# ir para o campo Área da propriedade - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

# Digitar valor
keyboard.write('7000')
pyautogui.hotkey('tab')

# Aguarde um curto período
# ir para o campo Área da Propriedade - Arrendada(ha)
# Digitar valor
pyautogui.sleep(0.3)
keyboard.write('6000')

# ir para o campo Área Produtiva - Própria(ha)
# Digitar valor
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
keyboard.write('7000')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

# ir para o campo Área Produtiva - Arrendada(ha)
# Digitar valor
keyboard.write('6000')
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# clicar no botão prosseguir
pyautogui.hotkey('enter')

# TELA REBANHO
# ir para campo Vacas (Lactação)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('50')

# ir para campo Vacas (Secas)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('50')

# ir para campo Fêmeas 0-12 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('20')

# ir para campo Fêmeas 13-24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('30')

# ir para campo Fêmeas 25-36 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('45')

# ir para campo Fêmeas +36 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('45')

# MACHOS
# ir para campo Reprodutores
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('5454')

# ir para campo RUFIÕES
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('10')

# ir para campo Machos 0-12 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('487')

# ir para campo Machos 13-24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('345')

# ir para campo Machos +24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para botão PROSSEGUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Clicar em enter
# ir para botão PROSSEGUIR
pyautogui.hotkey('enter')

# Aba PRODUÇÃO DE LEITE
# ir para campo Vacas em Lactação (Cab/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('300')

# ir para campo Produtividade (l/vaca/dia)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('6000')

# ir para campo Leite para Consumo (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('4545')

# ir para campo Leite para Descarte (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('5644')

# ir para campo Leite para Aleitamento (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para campo Média de Preço de Venda do Leite (R$/l)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('399')

# ir para campo CCS (Células/mL)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para campo CBT (UFC/mL)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para campo Média de Bonificação no Preço do Leite (R$/l)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para BOTÃO PROSSEGUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# clicar no BOTÃO PROSSEGUIR
pyautogui.hotkey('enter')

# Aguarde um curto período
pyautogui.sleep(0.3)

# ABA COMERCIALIZAÇÃO
# ir para campo Custo Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('7897898')

# ir para campo Custo Operacional Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('5464544')

# ir para campo Custo Operacional Efetivo Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('2312312')

# ir para BOTÃO CONCLUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)

# clicar no BOTÃO CONCLUIR
pyautogui.hotkey('enter')

# - Preenchimento da aba Bovinocultura de leite:
# Atividade Rural
# Condomínio Agropecuário

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.3)
pyautogui.hotkey('ctrl', 'end')

# Aguarde um curto período
pyautogui.sleep(0.3)

# Clicar botão Preencher ano (2024)
pyautogui.click(1616, 562, duration=0.3)

# ir para campo Sistema de Produção
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Extensivo)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.3)

# ir para campo Sistema de Ordenha
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Mecânico)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.3)

# ir para campo Tipo de Atividade Leiteira
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# Selecionar opção (Produção de leite)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.press('enter')

# Aguarde um curto período
pyautogui.sleep(0.3)
# ir para o campo Área da propriedade - Própria(ha)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

# Digitar valor
keyboard.write('7000')
pyautogui.hotkey('tab')

# Aguarde um curto período
# ir para o campo Área da Propriedade - Arrendada(ha)
# Digitar valor
pyautogui.sleep(0.3)
keyboard.write('6000')

# ir para o campo Área Produtiva - Própria(ha)
# Digitar valor
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
keyboard.write('7000')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)

# ir para o campo Área Produtiva - Arrendada(ha)
# Digitar valor
keyboard.write('6000')
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# clicar no botão prosseguir
pyautogui.hotkey('enter')

# TELA REBANHO
# ir para campo Vacas (Lactação)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('50')

# ir para campo Vacas (Secas)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('50')

# ir para campo Fêmeas 0-12 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('20')

# ir para campo Fêmeas 13-24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('30')

# ir para campo Fêmeas 25-36 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('45')

# ir para campo Fêmeas +36 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('45')

# MACHOS
# ir para campo Reprodutores
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('5454')

# ir para campo RUFIÕES
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('10')

# ir para campo Machos 0-12 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('487')

# ir para campo Machos 13-24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('345')

# ir para campo Machos +24 meses
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para botão PROSSEGUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Clicar em enter
# ir para botão PROSSEGUIR
pyautogui.hotkey('enter')

# Aba PRODUÇÃO DE LEITE
# ir para campo Vacas em Lactação (Cab/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('300')

# ir para campo Produtividade (l/vaca/dia)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('6000')

# ir para campo Leite para Consumo (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('4545')

# ir para campo Leite para Descarte (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('5644')

# ir para campo Leite para Aleitamento (l/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para campo Média de Preço de Venda do Leite (R$/l)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('399')

# ir para campo CCS (Células/mL)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para campo CBT (UFC/mL)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para campo Média de Bonificação no Preço do Leite (R$/l)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('129')

# ir para BOTÃO PROSSEGUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# clicar no BOTÃO PROSSEGUIR
pyautogui.hotkey('enter')

# Aguarde um curto período
pyautogui.sleep(0.3)

# ABA COMERCIALIZAÇÃO
# ir para campo Custo Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('7897898')

# ir para campo Custo Operacional Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('5464544')

# ir para campo Custo Operacional Efetivo Total (R$/ano)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
# Digitar valor
keyboard.write('2312312')

# ir para BOTÃO CONCLUIR
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)
pyautogui.hotkey('tab')

# Aguarde um curto período
pyautogui.sleep(0.3)

# clicar no BOTÃO CONCLUIR
pyautogui.hotkey('enter')

# clicar na aba Propriedades Rurais

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.3)
pyautogui.hotkey('ctrl', 'end')

pyautogui.click(249, 439, duration=0.3)

# Rolar para baixo imediatamente
pyautogui.click(1616, 320, duration=0.3)
pyautogui.hotkey('ctrl', 'end')

# clicar no botão Adicionar Propriedade
pyautogui.click(1695, 257, duration=0.3)

# clicar na combo Tipo da propriedade
pyautogui.click(1545, 243, duration=0.3)

# selecionar Própria
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.sleep(0.3)

# Ir para o campo Matrícula
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para matrícula
keyboard.write('56451')
pyautogui.sleep(0.3)

# Ir para o campo CCIR
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para CCIR
keyboard.write('5641446841234')
pyautogui.sleep(0.3)

# Ir para o campo CAR
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para CAR
keyboard.write('AS5456')
pyautogui.sleep(0.3)

# Ir para o campo LATITUDE
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para LATITUDE
keyboard.write('85645')
pyautogui.sleep(0.3)

# Ir para o campo Longitude
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para Longitude
keyboard.write('85645')
pyautogui.sleep(0.3)

# Ir para o campo Nome da Fazenda
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para Nome da Fazenda
keyboard.write('85645')
pyautogui.sleep(0.3)

# Ir para o campo UF
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor UF
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para o campo município
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor município
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para o campo Área Total (ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para Área Total (ha)
keyboard.write('85645')
pyautogui.sleep(0.3)

# Ir para o campo Área Produtiva (ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para Área Produtiva (ha)
keyboard.write('85645')
pyautogui.sleep(0.3)

# Ir para o campo Número de Safras por Ano
pyautogui.hotkey('tab')
# preencher valor para Número de Safras por Ano
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para o campo Área Irrigada (ha)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para Área Irrigada (ha)
keyboard.write('85645')
pyautogui.sleep(0.3)

# Ir para o campo Reserva Legal (ha)
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para Reserva Legal (ha)
keyboard.write('85645')
pyautogui.sleep(0.3)

# Ir para o campo Atividade Principal
pyautogui.hotkey('tab')
# preencher valor Atividade Principal
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para o campo Valor Terra Nua/ha (R$)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para Valor Terra Nua/ha (R$)
keyboard.write('85645')
pyautogui.sleep(0.3)

# Ir para o campo Área Georeferenciada
pyautogui.hotkey('tab')
# preencher valor Área Georeferenciada (SIM)
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para o campo Solo Predominante
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# preencher valor Solo Predominante
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para o campo Sobreposição com Terras Indígenas, Assentamentos, Quilombolas ou Áreas de Conservação
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# preencher valor Sobreposição com Terras Indígenas, Assentamentos, Quilombolas ou Áreas de Conservação
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para o campo Cartório de Registro do Imóvel
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para Cartório de Registro do Imóvel
keyboard.write('85645')
pyautogui.sleep(0.3)

# Ir para o campo Sócios
pyautogui.hotkey('tab')
# preencher valor Sócios
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para o campo Hipoteca
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# preencher valor Hipoteca
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para o campo Alienação Fiduciária
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
# preencher valor Alienação Fiduciária
pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# Ir para o campo Confrontantes
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.sleep(0.3)
# preencher valor para Confrontantes
keyboard.write('85645')
pyautogui.sleep(0.3)

# Clicar no botão Salvar Propriedade
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
pyautogui.sleep(0.3)

# clicar no botão SOLICITAR RARO
# pyautogui.click(1732,984, duration=0.3)

# Rodando em 2:49 minutos