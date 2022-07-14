# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:44:52 2020

@author: dell
"""
import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5,6,20])
y=np.array([2,5,6,1,2,9,20])
plt.plot(x)
#plt.show()


plt.plot(x,y)
plt.grid(True)
#plt.show()

plt.plot(x,y,'gs')
plt.grid(True)
plt.axis([0,20,0,20])
plt.show()

"""
 plt.plot(x,10,'ro',x,10*2,'g^')
 plt.ylabel('Y')
 plt.xlabel('El balor de mi arreglo')
 plt.show()
"""