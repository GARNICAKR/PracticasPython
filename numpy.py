# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:20:34 2020

@author: dell
"""

import numpy as np
a=np.array([2,3,4,5,6])
b=np.array([10,11,12,13,14])
print(a+b)
print(a*b)
print (a**b)



print (type (a))
print(a.ndim)
print (a.dtype)
print (a.shape)
print (a.itemsize)
print (a.nbytes)
print (a.size)


r=np.random.random((3,3,4))
print(r)
print (r.ndim)
print(r.shape)

c=np.arange(1,20,2)
print(c)
c=np.linspace(1,20,20)
print(c)
