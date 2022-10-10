# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:49:30 2019

@author: aluno
"""
import numpy as np
import hidroweb as hid
import matplotlib.pyplot as plt

hid.hidroweb_para_colunas("vazoes_T_65025000.txt","65025000_V2.txt")


arq1 = np.genfromtxt("65025000.txt",\
                     dtype= [('NC','i8'),('Data','M8[D]'),('dado','f8')],\
                     delimiter=";",\
                     skip_header=1)
Q=arq1['dado']
Q_sem_falhas=Q[Q!=-999]
#Q_ord= np.sort(Q_sem_falhas)
Q_ord2= sorted(Q_sem_falhas, reverse=True)

fr=np.ones(len(Q_ord2))/(len(Q_ord2)+1)
fr_acum=np.cumsum(fr)
perm=fr_acum*100.0

plt.plot(perm, Q_ord2)
plt.title("Curva de Permanência")
plt.xlabel("Frequência (%)")
plt.ylabel("Vazão (m³/s)")
plt.savefig("cp.png", dpi=300)





##CURVA DE PERMANENCIA
#cp = pd.read_csv("cp.csv", sep=";")
#y=cp['vazao']
#y1= y.sort_values(ascending=False)
#print(y1)
#
#x1=[]
#for i in range(len(y1)):
#    p=i*100/(len(y1)+1)
#    x1.append(p)
#    
#plt.plot(x1,y1)
#plt.title("Curva de permanência")
#plt.xlabel("Frequência (%)")
#plt.ylabel("Vazão (m³/s)")
#plt.savefig("cp.png", dpi=300)
#
#
