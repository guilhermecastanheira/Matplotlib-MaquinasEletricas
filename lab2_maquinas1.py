# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:58:43 2020

@author: User
"""

import matplotlib.pyplot as plt

#independente
Vi=[220.6, 218.7, 216.4, 214.1, 211.5, 208.7, 205.3, 202.3, 199.1, 194.2]
Ii=[0, 0.143, 0.304, 0.451, 0.595, 0.748, 0.908, 1.044, 1.192, 1.392]

#shunt
Vs=[220, 215.7, 211.9, 207.7, 203.0, 198.5, 192.6, 185.1, 179.1, 170.8]
Is=[0, 0.141, 0.294, 0.451, 0.602, 0.745, 0.902, 1.075, 1.205, 1.343]

#composta ativa
Vca=[147.8, 152.5, 160.1, 169.5, 180, 191.1, 191.2, 191.4, 192.6, 193.6]
Ica=[0, 0.104, 0.233, 0.413, 0.699, 1.175, 1.204, 1.269, 1.34, 1.381]

#composta subtrativa
Vcs=[220.7, 211.8, 198.1, 192, 184.8, 171.8, 152.8, 116.1, 85, 6.21]
Ics=[0, 0.139, 0.301, 0.36, 0.413, 0.494, 0.569, 0.619, 0.584, 0.286]

plt.figure(1)
plt.title('Curvas de Carga')
plt.xlabel('Corrente - It (A)')
plt.ylabel('Tensão - Vt (V)')
plt.plot(Ii, Vi, 'o-', label='Independente')
plt.plot(Is, Vs, 'o-', label='Shunt')
plt.plot(Ica, Vca, 'o-', label='Composta Aditiva')
plt.plot(Ics, Vcs, 'o-', label='Composta Subtrativa')
plt.legend();
plt.grid(True)
plt.show()




