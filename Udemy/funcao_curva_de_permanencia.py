# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 08:30:56 2019

@author: L01172
"""


import matplotlib.pyplot as plt
import pandas as pd

#CURVA DE PERMANENCIA
cp = pd.read_csv("cp.csv", sep=";").dropna()
y=cp['vazao']

#def c_perm(y):
y1= y.sort_values(ascending=False)
print(y1)

x1=[]
q95 = []
for i in range(len(y1)):
    p=i*100/(len(y1)+1)
    x1.append(p)
    
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

#c_perm(y)

# TESTE UNIFICANDO SUBPLOTS
fig, axarr = plt.subplots(2, 2)
fig.suptitle("Curvas de permanência", fontsize=16)

axarr[0, 0].plot(x1,y1)
axarr[0, 0].scatter(95, q95, color = 'r')
axarr[0, 0].text(x= 45, y=400, s=texto)
axarr[0, 0].set_title('Estação 1')
axarr[0, 1].plot(x1,y1)
axarr[0, 1].scatter(95, q95, color = 'r')
axarr[0, 1].text(x= 45, y=400, s=texto)
axarr[0, 1].set_title('Estação 2')
axarr[1, 0].plot(x1,y1)
axarr[1, 0].scatter(95, q95, color = 'r')
axarr[1, 0].text(x= 45, y=400, s=texto)
axarr[1, 0].set_title('Estação 3')
axarr[1, 1].plot(x1,y1)
axarr[1, 1].scatter(95, q95, color = 'r')
axarr[1, 1].text(x= 45, y=400, s=texto)
axarr[1, 1].set_title('Estação 4')

# # Fine-tune figure; hide x ticks for top plots and y ticks for right plots
plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

# Tight layout often produces nice results
# but requires the title to be spaced accordingly
fig.tight_layout()
fig.subplots_adjust(top=0.8)
plt.savefig("suplots_cp.png", dpi=300)
plt.show()



# TESTE UNIFICANDO SUBPLOTS  GRUDADINHO

texto2="Q95 = "+ str("%.2f" % (2*q95)) + " m³/s"
fig, axarr = plt.subplots(2, 2, sharex='col', sharey='row',
                        gridspec_kw={'hspace': 0, 'wspace': 0})
fig.suptitle("Curvas de permanência", fontsize=16)
fig.text(x= 0.04, y= 0.5, s="Vazão (m³/s)", fontsize=10, rotation= 90, ha='center', va= 'center')
fig.text(x= 0.5, y= 0.04, s="Frequência (%)", fontsize=10, ha='center', va= 'center')
axarr[0, 0].plot(x1,y1)
axarr[0, 0].scatter(95, q95, color = 'r')
axarr[0, 0].text(x= 45, y=600, s=texto)
axarr[0, 0].text(x= 35, y=1080, s="Estação 1")
axarr[0, 0].set_ylim(0, 600)
axarr[0, 1].plot(x1,2*y1, color = '#33ff33')
axarr[0, 1].scatter(95, 2*q95, color = 'r')
axarr[0, 1].text(x= 45, y=600, s=texto2)
axarr[0, 1].text(x= 35, y=1080, s="Estação 2")
axarr[0, 1].set_ylim(0, 1200)
axarr[1, 0].plot(x1,y1)
axarr[1, 0].scatter(95, q95, color = 'r')
axarr[1, 0].text(x= 45, y=300, s=texto)
axarr[1, 0].text(x= 35, y=630, s="Estação 3")
axarr[1, 0].set_ylim(0, 700)
axarr[1, 1].plot(x1,y1)
axarr[1, 1].scatter(95, q95, color = 'r')
axarr[1, 1].text(x= 45, y=300, s=texto)
axarr[1, 1].text(x= 35, y=630, s="Estação 4")
axarr[1, 1].set_ylim(0, 700)

# # Fine-tune figure; hide x ticks for top plots and y ticks for right plots
plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

# Tight layout often produces nice results
# but requires the title to be spaced accordingly
#fig.tight_layout()
fig.subplots_adjust(top=0.9)

plt.savefig("suplots_cp_2.png", dpi=400)
plt.show()
