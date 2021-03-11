# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 14:20:17 2020

@author: guilhermecastanheira
"""

import matplotlib.pyplot as plt

#SHUNT

#Ea shunt crescente 
Easc = [33.75, 50, 76.7, 99.2, 124.9, 149.6, 176.1, 200.2, 219.8, 238.5]

#If shunt crescente
Ifsc = [0, 0.021, 0.048, 0.066, 0.088, 0.112, 0.143, 0.179, 0.217, 0.266]

#Ea shunt decescente
Easd = [241.7, 221.6, 201.0, 175, 147.7, 126.4, 100.8, 75.5, 47.8, 33.59]

#If shunt decrescente
Ifsd = [0.275, 0.209, 0.161, 0.120, 0.089, 0.069, 0.047, 0.028, 0.01, 0]

plt.figure(1)
plt.title('Curva de Magnetização - Enrolamento SHUNT')
plt.xlabel('Corrente de Campo - If (A)')
plt.ylabel('Tensão de Armadura - Ea (V)')
plt.plot(Ifsc, Easc, 'b')
plt.plot(Ifsd, Easd, 'r')
plt.legend(['Crescente', 'Decrescente'])
plt.grid(True)
plt.show()


#SERIE

#Ea serie crescente
Eac = [33.59, 47.6, 62.4, 81, 98.9, 117.2, 136.7, 151, 166.5, 184.1]

#If serie crescente
Ifc = [0, 0.237, 0.428, 0.624, 0.806, 1, 1.232, 1.414, 1.638, 1.93]

#Ea serie decrescente
Ead = [184.2, 173.2, 164.2, 150.5, 139.2, 121.4, 100.7, 77.2, 58.6, 33.52]

#If serie decrescente
Ifd = [1.928, 1.667, 1.485, 1.25, 1.086, 0.862, 0.625, 0.394, 0.235, 0.012]

plt.figure(2)
plt.title('Curva de Magnetização - Enrolamento SÉRIE')
plt.xlabel('Corrente de Campo - If (A)')
plt.ylabel('Tensão de Armadura - Ea (V)')
plt.plot(Ifc, Eac, 'g')
plt.plot(Ifd, Ead, 'm')
plt.legend(['Crescente', 'Decrescente'])
plt.grid(True)
plt.show()