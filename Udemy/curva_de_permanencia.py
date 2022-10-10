# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:14:13 2019

@author: Ana Becker
"""

import matplotlib.pyplot as plt
import pandas as pd

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
data['Index2'] = r
data= data.set_index('Index2')
data['Freq'] = x1
q=data.loc[lambda data: data.Freq > 95, :]
r2 = list(range(len(q)))
q['Index2'] = r2
q= q.set_index('Index2')
q95= q.loc[0,'Vazao']

#CURVA DE PERMANENCIA #  2
texto= "Q95 = "+ str("%.2f" % q95) + " m³/s"
plt.plot(x1,y1)
plt.scatter(95, q95, color = 'r')
plt.text(x= 70, y=400, s=texto)
plt.title("Curva de permanência")
plt.xlabel("Frequência (%)")
plt.ylabel("Vazão (m³/s)")
plt.savefig("cp.png", dpi=300)
plt.show()
