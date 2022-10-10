# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:16:56 2019
@author: Ana Paula Muhlenhoff

Aula 1 - Condicionais
Aula 2 - Funções bissexto e dias_mes
Aula 3 - Leitura do cabeçalho do arquivo do hidroweb - vazões
Aula 4 - Leitura dos dados do arquivo de vazões e escrita de um arquivo em colunas

"""
def bissexto(ano):
    """ Função recebe o valor do ano (inteiro)
        Retorna True se o ano é bissexto
        Retorna False se o ano não é bissexto."""
    
    if ano % 4.0 == 0.0 and ano % 100.0 != 0.0:
        return True
    elif ano % 400.0 == 0:                                                      # Testa se é divisível por  400
        return True                                                             # Se é divisivel por 400 é bissexto
    else:
        return False 


def dias_mes(mes, ano):
    """
    Função recebe mês e ano
    Retorna o número de dias do mês para aquele ano.
    """
    if mes in [1, 3, 5, 7, 8, 10, 12]:                                          # Meses com 31 dias
        dias = 31
    elif mes == 2:                                                              # Fevereiro
        if bissexto(ano) == True: 
            dias = 29
        else:
            dias = 28
    else:                                                                       # Meses com 30 dias
        dias = 30
    
    return dias

def hidroweb_para_colunas(nome_arquivo_entrada, nome_arquivo_saida):
    """
    Função recebe um nome de arquivo para leitura e retorna 
    um outro arquivo, na mesma pasta, com os dados brutos transcritos em colunas
    de data, nível de consistência e dado observado
    """
    # Abre o arquivo para leitura
    arquivo = open(nome_arquivo_entrada, 'r')
    
    # Lê as linhas de cabeçalho, uma a uma
    titulo = [0]
    while titulo[0] != 'EstacaoCodigo':
        titulo = arquivo.readline().split(';')
    
    # Lê todas as linhas de dados
    conteudo = arquivo.readlines()
    
    # Fecha o arquivo aberto para leitura
    arquivo.close()
    
    # Retira das linhas do arquivo os dados que precisamos: data, nivel consistência e vazão
    lista_registros = []
    for linha in conteudo:
        l = linha.split(';')                                                        # l é um objeto do tipo lista
        registro = l[1:3] + l[16:47]                                                # registro = list(l[1]) + list(l[2]) + l[16:47]
    
        # Cada registro é uma lista que contêm o mês de dados de um ano o nível de consistência e os valores medidos de vazão
        lista_registros.append(registro)
    
    # Abre um arquivo novo, para escrever os registros em colunas
    arquivo_saida = open(nome_arquivo_saida, 'w')
    
    # Escreve o cabeçalho no arquivo de saída
    arquivo_saida.write('Nivel de consistência; Data; Vazão\n')
    
    # Laços para ordenar os dados em colunas
    for l1 in lista_registros:
        
        # Separo a string da data em uma lista com [dia, mês, ano]
        data = l1[1].split('/')
        
        # Armazeno como inteiros os valores de mês e ano
        mes = int(data[1])
        ano = int(data[2])
        
        # Com o mês e ano descubro quantos dias tem aquele mês chamando a função dias_mes
        dias = dias_mes(mes, ano)
        
        # Inicio um contador para correr os dias do mês e pegar o dado de vazão correspondente
        d = 0
        
        # Inicio o laço para escrever para cada dia, uma linha no arquivo de saída
        while d < dias:
            dia_obs = d + 1
            dado_obs = l1[(d + 2)].replace(',','.')
            
            # Inserindo código de falha
            if dado_obs == '':
                dado_obs = '-999'
            elif dado_obs == '0':
                dado_obs = '-999'
            
            # Defino um separador para os elementos na linha de saída
            sep = ';'
            
            # Monto a data como uma string
#            data_obs = str(dia_obs) + ';' + str(mes) + ';' + str(ano)
#            if len(str(mes)) == 1:
#                M = '0' + str(mes)
            if len(str(dia_obs)) == 1:
                D = '0' + str(dia_obs)
                
            data_obs = str(ano) + '-' + data[1] + '-' + D
            # Montamos a linha de saída
            saida = l1[0] + sep + data_obs + sep + dado_obs + '\n'
            
            # Escreve uma linha no arquivo de saída
            arquivo_saida.write(saida)
            
            # Incremento para o laço while
            d = d + 1
    
    # Fecha o arquivo que foi aberto para escrever os resultados. (Saindo do laço - arquivo todo já escrito.) 
    arquivo_saida.close()
    
    return 


hidroweb_para_colunas('cotas_T_56994500.txt', '56994500.txt')







