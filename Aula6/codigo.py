# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np
import matplotlib.pyplot as plt

def bissexto(ano):    
    if ano % 4 == 0.0 and ano % 100.0 != 0.0:
            return True
    elif ano % 400 == 0.0:
        return True
    else:
        return False

def dias_mes(mes, ano):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        dias = 31
    elif mes == 2:
        if bissexto(ano) == True:
           dias = 29
        else:
            dias = 28
    else:
        dias = 30
    return dias 

# biblioteca pandas para ler arquivos
arquivo = open('F:/CursoPhyton/Aula4/vazoes_T_65025000.txt','r')
#na saída é w
titulo = [0]
while titulo[0] != 'EstacaoCodigo':
    # titulo[0] primeiro elemento da lista titulo
    titulo = arquivo.readline().split(';')
#le todas as linhas que nao leu ainda
conteudo = arquivo.readlines() 

arquivo.close

lista_registros=[]
for linha in conteudo:
    l = linha.split(';') #l é um objeto tipo lista (separou a linha)
    registro = l[1:3] +l[16:47]  #inclui 16 mas não inclui 47     concatena
    lista_registros.append(registro)
    
arquivo_saida = open('65025000.txt','w')
arquivo_saida.write('cons;dia;mes;ano;vazao\n')
for l1 in lista_registros:
    data = l1[1].split('/')
    mes = int(data[1])
    ano = int(data[2])
    dias= dias_mes(mes,ano)
    
    d=0 #no while eu tenho que criar um contador antes de iniciar o laço
    while d < dias:
        dia_obs = d + 1
        dado_obs = l1[d+2].replace(",",".")
        
        sp=';'
        data_obs = str(dia_obs) + ';' + str(mes) + ';' + str(ano)
        saida = l1[0] + sp + data_obs + sp + dado_obs + '\n'   #'\n pula linha
        arquivo_saida.write(saida)
        d = d + 1

arquivo_saida.close()

arq1 = np.genfromtxt("65025000.txt",  delimiter=";", skip_header=1)
#c2 = arq1.readlines() 

#plt.boxplot(dado_obs)

