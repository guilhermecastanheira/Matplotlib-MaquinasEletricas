# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:28:43 2021

@author: User
"""

import sys
import matplotlib.pyplot as plt 

#crescente
Ic = [0, 0.225, 0.262, 0.289, 0.35, 0.55, 0.657, 0.924, 1.427, 1.777]
Vc = [2.678, 39.31, 45.7, 50.7, 61.8, 95.2, 111.5, 147.2, 196.3, 221.8]

#decrescente
Id = [1.774, 1.28, 1.022, 0.855, 0.549, 0.339, 0.279, 0.251, 0.216, 0]
Vd = [222.9, 187.1, 160.5, 140, 96.9, 61.9, 51.3, 46.4, 39.6, 2.68]

plt.figure(1)
plt.title("Curva de Magnetização - Gerador Síncrono")
plt.xlabel("If [A]")
plt.ylabel("Vab [V]")
plt.plot(Ic,Vc,'o-',color='b', label="Crescente")
plt.plot(Id,Vd,'o-',color='r', label="Decrescente")
plt.legend()
plt.grid(True)
plt.show()