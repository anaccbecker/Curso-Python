# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
# for 
    
#for cont in [1, 2, 3, 4, 5]:
#    cont = cont +1
#    print (cont)
    
# while
    
#i = 10.5
#while i != 0:
#    i = i - 1 
#    print(i)
    
    

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
arquivo = open('C:/Users/aluno/Desktop/CursoPhyton/Aula3/vazoes_T_65025000.txt','r')
#na saída é w
titulo = [0]
while titulo[0] != 'EstacaoCodigo':
    # titulo[0] primeiro elemento da lista titulo
    titulo = arquivo.readline().split(';')
conteudo = arquivo.readlines()

arquivo.close
