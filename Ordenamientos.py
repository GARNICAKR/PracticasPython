# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:42:07 2020

@author: dell
"""
from timeit import timeit
from time import time
import numpy as np
import matplotlib.pyplot as plt
import random
def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        #print(izquierda+["-"]+centro+["-"]+derecha)
        return sort(izquierda)+centro+sort(derecha)
    else:
      return lista
def mergesort(lista):
        if(len(lista)>1):
            m=len(lista)//2
            izq=lista[:m]
            der=lista[m:]
            i=j=k=0
            izq=mergesort(izq)
            der=mergesort(der)
            while(i<len(izq)and j<len(der)):
                if(izq[i]<=der[j]):
                    lista[k]=izq[i]
                    i+=1
                    k+=1
                else:
                    lista[k]=der[j]
                    j+=1
                    k+=1
            while(i<len(izq)):
                lista[k]=izq[i]
                i+=1
                k+=1
            while(j<len(der)):
                lista[k]=der[j]
                j+=1
                k+=1
            return lista
        else:

            return lista
merge_es=[]
lista=[]
i=0
j=1
while(j<9):
    while(i<10**j):
        lista.append(random.randint(0,99))
        i+=1
    start_time = time()
    mergesort(lista)
    elapsed_time = time() - start_time
    merge_es.append(elapsed_time)
    j+=1
    i=0
plt.plot(merge_es,'gs')
plt.grid(True)
plt.plot(merge_es)
plt.show()

print("ist over")