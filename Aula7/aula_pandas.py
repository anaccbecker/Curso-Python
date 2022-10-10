import pandas as pd
import matplotlib.pyplot as plt

# Cria um dataframe vazio
dt_1 = pd.DataFrame()

# Adiciona colunas no dataframe
dt_1['Nome'] = ['João', 'Degraf', 'Jéssica', 'Arthur', 'Bia', 'Cris']
dt_1['Idade Real'] = [22, 22, 35, 25, 22, 50]
dt_1['Idade Aparente'] = [85, 16, 35, 28, 19, 50]

# Nova culona a partir de uma relação entre colunas existentes
dt_1['Diferença Abs'] = abs(dt_1['Idade Real'] - dt_1['Idade Aparente'])

# Coloca como 'cabeçalho' a coluna Nome
dt_1 = dt_1.set_index('Nome')

# Faz o plot de todas as colunas do dataframe
dt_1.plot.bar()
plt.show()

# Faz o plot de todas as colunas do dataframe - GRÁFICOS SEPARADOS
dt_1.plot.bar(subplots=True)
plt.show()

# Nome dos arquivos a serem lidos
file_1 = 's_vazoes_T_64005000.txt'
file_2 = 's_vazoes_T_64275000.txt'

# Cria duas listas para armazenamento
list_file = [file_1, file_2]
list_dts = []

# Itera entre os arquivos
for file in list_file:
    # Cria o dataframe a partir de um csv
    # sep=";" - Separador decimal que o arquivo contém
    # header=[9] - Número da linha em que a matriz de dados começa
    # engine='python'
    # decimal="," - Separador decimal que o arquivo usa
    dt = pd.read_csv(file, sep=";", header=[9], engine='python', decimal=",")

    # Separa só as colunas de interesse - Data, nível de consistência e Vazão
    dt = dt[['Data', 'NivelConsistencia', 'Vazao']]

    # Acerta o formato da data
    dt['Data'] = pd.to_datetime(dt['Data'], format='%d/%m/%Y')

    # Coloca a Data como index do dataframe
    dt = dt.set_index('Data')

    # Organiza o dataframe por ordem decrescente em relação ao INDEX
    dt = dt.sort_index()

    # Exclui a coluna Nivel de Consistencia
    dt = dt.drop(columns=['NivelConsistencia'])

    # Adiciona o dataframe para a lista
    list_dts.append(dt)

# Concatena os dataframes dentro da lista
dt_final = pd.concat(list_dts, axis=1)

# Renomeia as colunas do dataframe
dt_final.columns = ['Estação 1', 'Estação 2']

# Executa o plot dos dados como anteriormente
dt_final.plot()
plt.show()

# Reorganiza o dataframe para formato anual, adotando o valor MÉDIO do ano
dt_final = dt_final.groupby(pd.Grouper(freq='Y')).mean()

# Executa o plot dos dados como anteriormente
dt_final.plot.bar()
plt.show()

# Exclui toda linha que contenha um valor NaN ( Not a Number)
dt_final = dt_final.dropna()
dt_final.plot.bar()
plt.show()

# Salva o dataframe como txt
dt_final.to_csv('teste.txt')