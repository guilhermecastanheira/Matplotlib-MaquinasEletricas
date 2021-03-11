# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:25:16 2021

@author: User
"""

import sys
import numpy as np
import matplotlib.pyplot as plt 

sys.getdefaultencoding()

omega = '\u03A9'

#dados
If = [0, 0.31, 0.52, 0.55, 0.63, 0.79, 1.09, 1.32, 1.51, 1.65]
Va = [2.58, 53.1, 91.6, 106.2, 120.1, 155.8, 195.1, 217, 225.9, 234.7]
Icc = [0.015, 0.305, 0.507, 0.583, 0.659, 0.881, 1.227, 1.419, 1.557, 1.699]
Xs = [172, 174.1, 180.7, 182.2, 182.2, 176.8, 159, 152.9, 145.1, 138.1]

fig, ax1 = plt.subplots()

ax1.set_xlabel("If [A]")
ax1.set_ylabel("Va [V]  ;  Xf [\u03A9]")
ax1.plot(If, Va, 'o-',color='r', label="Va x If : curva de circuito aberto")
ax1.plot(If, Xs, 'o-',color='g', label="Xs x If : curva de reatência síncrona")
ax1.legend()
ax1.grid(color='gray', linestyle='--', linewidth=0.5)

ax2 = ax1.twinx()
ax2.set_ylabel("Icc [A]")
ax2.plot(If, Icc, 'o-',color='b', label="Icc x If : curva de curto-circuito")
ax2.legend(loc='lower right')

plt.title("Ensaios a vazio e curto circuito - Reatância Síncrona")
plt.show()
