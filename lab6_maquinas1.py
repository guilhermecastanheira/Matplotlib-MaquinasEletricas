# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 08:25:35 2021

@author: User
"""

import sys
import numpy as np
import matplotlib.pyplot as plt 

sys.getdefaultencoding()

fi = '\u03C6'

# Questao 2 - 50W
Ia50=[0.551, 0.367, 0.294, 0.221, 0.432, 0.543, 0.675]
If50=[0.881, 0.904, 0.926, 0.961, 1.032, 1.055, 1.085]

# Questao 3 - 300W
Ia300=[1.112, 0.801, 0.653, 0.561, 0.895, 1.141, 1.422]
If300=[0.871, 0.902, 0.942, 1.041, 1.139, 1.197, 1.261]

# Questao 4 - 600W
Ia600=[1.81, 1.38, 1.19, 1.14, 1.61, 1.94, 2.21]
If600=[0.852, 0.906, 0.967, 1.031, 1.312, 1.412, 1.481]

# Questao 5 - cos(fi) unitario
Ia=[0.312, 0.427, 0.589, 0.696, 0.868, 1.215, 1.602, 1.991]
If=[0.932, 0.948, 0.968, 0.978, 0.998, 1.04, 1.06, 1.077]


plt.figure(1)
plt.title('Curvas "V" - Gerador Síncrono')
plt.xlabel("If [A]")
plt.ylabel("Ia [A]")
plt.plot(If,Ia,'o-',color='b', label='cos(\u03D5) unitário')
plt.plot(If600,Ia600,'o-',color='r', label='Potência Nominal 600W')
plt.plot(If300,Ia300,'o-',color='g', label='Potência Média 300W')
plt.plot(If50,Ia50,'o-',color='m', label='Potência Mínima 50W')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
