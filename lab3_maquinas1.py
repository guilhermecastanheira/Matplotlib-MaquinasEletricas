# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 08:17:56 2020

@author: User
"""

import sys
import matplotlib.pyplot as plt 

sys.getdefaultencoding()

omega = '\u03C9 [rpm]'

#Torque
T = [0.05, 0.15, 0.225, 0.3, 0.525, 0.6375, 0.7, 0.8, 0.875, 1.2]

#corrente de armadura - Ia
Ia = [0.170, 0.256, 0.336, 0.4, 0.62, 0.73, 0.83, 0.92, 1.13, 1.4]

#velocidade omega
w = [1800, 1799, 1809, 1811, 1814, 1821, 1838, 1848, 1894, 1930]


plt.figure(1)
plt.xlabel("Ia [A]")
plt.ylabel("T [N.m]")
plt.plot(Ia,T,'*-',color='b')
plt.grid(True)
plt.show()

plt.figure(2)
plt.ylabel(omega)
plt.ylim(1000,2000)
plt.xlabel("T [N.m]")
plt.plot(T,w,'*-',color='r')
plt.grid(True)
plt.show()

