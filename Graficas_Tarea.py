# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 19:38:37 2020

@author: dell
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import cos,sin,pi
   

"""
x=np.array([-4,-3.5,-3,-2.5,-2,-1.5,-1,-.5,0,.5,1,1.5,2,2.5,3,3.5,4])
y=sin(x)
Y=cos(x)
p=-sin(x)
plt.plot(x,y)
plt.plot(x,Y)
plt.plot(x,p)
plt.grid(True)
plt.show()
"""




x=np.array([-5,-4.5,-4,-3.5,-3,-2.5,-2,-1.5,-1,-.5,0,.5,1,1.5,2,2.5,3,3.5,4,4.5,5])

y=sin(x)+x*cos(x)
Y=-1*(x*sin(x))+2*cos(x)
p=-1*(x*cos(x))-(3*sin(x))
plt.plot(x,y)
plt.plot(x,Y)
plt.plot(x,p)
plt.grid(True)
plt.show()