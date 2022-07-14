# -*- coding: utf-8 -*-
import time as tm
import matplotlib.pyplot as plt
import random
import numpy as np

def busquedaL (lista,elemento):
    for i in lista:
        if(lista[i]==elemento):
            return lista[i];
    return -1
    
def busquedaB(lista,elemento):
    cont=0;
    izq=0
    der=len(lista)-1
    mitad=len(lista)//2
    while(izq<=der):
        cont+=1
        mitad=(izq+der)//2
        if(lista[mitad]==elemento):
            return cont
        elif(elemento>lista[mitad]):
            izq=mitad+1
        else:
            der=mitad-1
    return cont

lista=[0,1,2,3,4,5,6,7,8,9]
num=busquedaB(lista,5)
print(num)
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
x=np.array([10000,50000,100000])
merge_es=[]
lineal=[]
lista=[]
i=0
j=4
while(j<7):
    lista=[]
    while(i<=10**j): 
        lista.append(i)
        i+=1
    start_time = tm.time()
    s=j-6*1000
    if(j>6):
        tm.sleep(.4)
   # print(busquedaB(lista,10**j))
    elapsed_time = tm.time() - start_time
    merge_es.append(busquedaB(lista,10**j))
    start_time = tm.time()
    if(j==7):
        tm.sleep(1)
    print(busquedaL(lista,10**j))
    elapsed_time = tm.time() - start_time
    lineal.append(10**j)
    j+=1
    i=0
   
#10 nodos minimo mostrar el nodo y 
#plt.plot(x,merge_es,'gs')
plt.grid(True)
plt.plot(x,merge_es)
plt.show()
print(merge_es)
#plt.plot(x,lineal,'gs')
plt.grid(True)
plt.plot(x,lineal)
plt.show()
print(lineal)

print("is over")