# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np

# LEITURA DE DADOS SEM BIBLIOTECA

#dados=open("populacao-brasileira.csv").readlines()
#x=[]
#y=[]
#for i in range(len(dados)):
#    if i !=  0:
#        linha = dados[i].split(";")
#        x.append(int(linha[0]))
#        y.append(int(linha[1]))
        
# LEITURA DE DADOS COM PANDAS     
df  = pd.read_csv("populacao-brasileira.csv", sep=";")
x=df['ano']
y=df['population']

#GRÁFICOS COM PANDAS
df.plot(x="ano",y="population")
df.plot.scatter(x="ano",y="population")
df.plot.hist(x="ano",y="population")

## GRÁFICO COM MATPLOTLIB
#LINHA
plt.plot(x,y) 
#BARRA
plt.bar(x,y, color = "#B0E0E6")
#BARRA HORIZONTAL        
#plt.barh(x,y, color = "#B0E0E6")
#PONTO      
plt.scatter(x,y, color="k") 
#boxplot
plt.boxplot(y,notch=x)

#SUBPLOT 
plt.subplot(3,1,1)
plt.plot(x,y) 
plt.subplot(3,1,2)
plt.bar(x,y, color = "#B0E0E6") 
plt.subplot(3,1,3)        
plt.scatter(x,y, color="k") 

#SUBPLOT 
plt.subplot(2,2,1)
plt.plot(x,y) 
plt.subplot(2,2,2)
plt.bar(x,y, color = "#B0E0E6") 
plt.subplot(2,2,3)        
plt.scatter(x,y, color="k") 

#TÍTULO E EIXOS
plt.title("População Brasileira")
plt.ylabel("População x 100.000.000")
plt.xlabel("Ano")
plt.savefig("fig1.png", dpi=300)
plt.show()


# TESTE UNIFICANDO SUBPLOTS
fig, axarr = plt.subplots(2, 2)
fig.suptitle("Tipos de gráfico", fontsize=16)

axarr[0, 0].plot(x, y)
axarr[0, 0].set_title('Linha')
axarr[0, 1].scatter(x, y)
axarr[0, 1].set_title('Ponto')
axarr[1, 0].bar(x,y, color = "#B0E0E6") 
axarr[1, 0].set_title('Barras Verticais')
axarr[1, 1].barh(x,y, color = "r") 
axarr[1, 1].set_title('Barras horizontais')

# # Fine-tune figure; hide x ticks for top plots and y ticks for right plots
plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

# Tight layout often produces nice results
# but requires the title to be spaced accordingly
fig.tight_layout()
fig.subplots_adjust(top=0.8)
plt.savefig("fig3.png", dpi=300)
plt.show()


#CURVA DE PERMANENCIA
cp = pd.read_csv("cp.csv", sep=";").dropna()
y=cp['vazao']
y1= y.sort_values(ascending=False)
print(y1)

x1=[]
q95 = []
for i in range(len(y1)):
    p=i*100/(len(y1)+1)
    x1.append(p)
    
plt.plot(x1,y1)
plt.title("Curva de permanência")
plt.xlabel("Frequência (%)")
plt.ylabel("Vazão (m³/s)")
plt.savefig("cp.png", dpi=300)

#CALCULAR O Q95
r = list(range(len(y1)))
data= pd.DataFrame()
data['Vazao'] = y1.sort_values(ascending=False)
data['Index'] = r
data.reset_index(drop=True)
data['Freq'] = x1


x2=[]
p=1
q95 = []
for i in range(len(y1)):
    while (p < 95):
        p=i*100/(len(y1)+1)
        x2.append(p)