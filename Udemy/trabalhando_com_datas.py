# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:58:21 2019

@author: L01172
"""

import matplotlib.pyplot as plt
import pandas as pd

#CURVA DE PERMANENCIA
cp = pd.read_csv("cp.csv", sep=";").dropna()
cp = cp.rename(columns={'ano': 'year', 'mes': 'month', 'dia': 'day'})
cp2= cp.loc[:,['year','month','day']]
datas= pd.to_datetime(cp2)
datas= datas.sort_values(ascending=True)
vazoes=cp['vazao']

plt.plot(datas,vazoes, linestyle='-', linewidth =0.3)
plt.title("Série Histórica da Estação")
plt.xlabel("Data")
plt.ylabel("Vazão (m³/s)")
plt.axhline(y=200, linestyle='--', color='r')
plt.savefig("data_vazoes.png",dpi=400)


plt.hist(vazoes)
plt.title("Série Histórica da Estação")
plt.xlabel("Vazão (m³/s)")
plt.ylabel("Frequência")
plt.axvline(x=200, linestyle='--', color='r')
plt.savefig("histograma.png",dpi=400)