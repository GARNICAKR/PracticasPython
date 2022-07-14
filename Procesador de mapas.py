# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:04:28 2020

@author: dell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:01:58 2019

@author: gabriel
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:49:30 2019

@author: gabriel
"""

import cv2
import numpy as np
from PIL import Image
"""
class Lista:
    Arista
class Arista:
    nodo = ''
    conex=
    def agregarN(self,dato):
        self.nodo=dato
    def agregarC(self,lista):
        self.conex=lista
"""
#cone sta funcion reviso si un punto ya esta en alguna de mis listas
def isInTheList(elemento,arreglo):
    for i in arreglo:
        if np.array_equal(i,elemento):
            return True            
    return False  
def Visitados(visitados,arista):
    contV=0
    x1=int(arista[0])
    y1=int(arista[1])
    for i in visitados:
      x2=int(visitados[contV][0])
      y2=int(visitados[contV][1])
      if x1 == x2:
          if y1==y2:
            return False
      contV+=1
    return True
def BuesquedaA(visitados,aristas,nodos,arbol):
    contVi=0
    Cord1=[]
    costo=1000000
    visi=[]
    elim=0
    for i in visitados:     
        contAr=0
        x1=int(visitados[contVi][0])
        y1=int(visitados[contVi][1])
        for j in aristas:
            x2=int(aristas[contAr][0][0])
            y2=int(aristas[contAr][0][1])
            if x1==x2:
                if y1==y2:
                    if Visitados(visitados,aristas[contAr][1]):
                        if costo>aristas[contAr][2]:
                            Cord1=visitados[contVi]
                            elim=contAr
                            costo=aristas[contAr][2]
                            visi=aristas[contAr][1]   
            contAr+=1
            if costo==1000000: 
                    if len(visitados)==contVi:
                        if len(aristas)==contAr:  
                            return False 
            
        contVi+=1
    #cv2.line(th2,tuple(i),tuple(j), (0,255,0),1)
    cv2.line(mapa,tuple(Cord1),tuple(visi),(0,0,255),1)
    arbol.append([Cord1,visi])
    aristas.pop(elim)
    visitados.append(visi)
    return True
    
    
def Conected (x1,y1,x2,y2,i):
    band=True
    x=int(abs(x1-x2)/2)
    y=int(abs(y1-y2)/2)
    if x1<x2:
        x=x+x1
    else:
        x=x1-x
    if y1<y2:
        y=y+y1
    else:
        y=y1-y
    
    b, g, r = th2[y, x]
    #print('pixel:', b, g, r)
    if b == 0:
        if g == 0:
            if r ==0:
                return False
    if i!=4:
        i+=1;
        band=Conected(x1,y1,x,y,i)
    if band==True:
       return True
    else:
       return False

#para cargar el mapa
mapa=cv2.imread('mapa4.png')
#pasamos la imagen a escala de grises
gray = cv2.cvtColor(mapa,cv2.COLOR_BGR2GRAY)
#muestro la imagen en escala de grises
cv2.imshow('mapa2',gray)
#obtengo un binarizacion en blaco todos lo pixeles cuyo valor en sea entre 254 y 255
ret,th1 = cv2.threshold(gray,254,255,cv2.THRESH_BINARY)
#hago un kernel de 11x11 de unos. Los Kernels se acostumbra hacerse de tamaño no par y cuadrados
#para que se den una idea algo asi:
"""
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
"""
kernel = np.ones((11,11), np.uint8) 
#aplico un filtro de dilatacion. Este filtro hace que los puntos los puntos blancos se expandan 
#probocando que algunos puntitos negros desaparecan #le pueden hacer un cv.imshow para que vean el resultado
th1 = cv2.dilate(th1,kernel,1)
kernel = np.ones((11,11), np.uint8) 
#Despues aplico uno de erosion que hace lo opuesto al de dilatacion
th1 = cv2.erode(th1,kernel,1)
#aplico un flitro gausiando de 5x5  para suavisar los bordes 
th1 = cv2.GaussianBlur(th1,(5,5),cv2.BORDER_DEFAULT) 
#muestro como queda mi mapa
cv2.imshow('thres',th1)
#Aplico la deteccion de Esquinas de Harris. para mas informacion consulten https://docs.opencv.org/3.4/dc/d0d/tutorial_py_features_harris.html
dst = cv2.cornerHarris(th1,2,3,0.05)
ret, dst = cv2.threshold(dst,0.04*dst.max(),255,0)
dst = np.uint8(dst)
ret,th2 = cv2.threshold(th1,235,255,cv2.THRESH_BINARY)
th2 = cv2.dilate(th2,kernel,1)
#aqui devuelvo la imagen binarizada a tres canales
th2 = cv2.cvtColor(th2,cv2.COLOR_GRAY2BGR)
# find centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst,30, cv2.CV_32S)
vertices=np.int0(centroids)    
aux1=vertices
aux2=vertices
conected=True
verticesConectados=[]
aristas=[]
cv2.imwrite('PIMA.png',th2)
im=Image.open('PIMA.png')
pixelMap = im.load()
#aqui voy a buscar cuales son las esquinas que estan conectadas
l=0;
nodos=[]
for h in range(len(aux1)):
    i=aux1[h]
    nodos.append([h,i])
for h in range(len(aux1)):
    i=aux1[h]
    for k in range(h,len(aux2)):
        j=aux2[k]
        if not (i==j).all():
         conected=Conected(i[0],i[1],j[0],j[1],0)
        if conected==True:  
             cv2.line(th2,tuple(i),tuple(j), (0,255,0),1)
             #print(i,end='')
             #print(j)
             x=int(abs(i[0]-j[0]))
             y=int(abs(i[1]-j[1]))
             
             if x<y:
                 aristas.append([i,j,y])
             else:
                 aristas.append([i,j,x])
             #print(Nodos,end='')    
             l+=1               
                #aqui deberian sacar los puntos de intermedios y verificar si i y j estan conectados
                #si estan conectados calcular el costo (la distancia en pixeles entre ellos) y agregarlos al grafo

#aqui yo dibujo mis lineas de las aristas de color verde, el uno es el grueso de la linea
#arista[0]   y arista[1]  tienen la forma de [fila, columna]
"""       
while contA!=l:
    cv2.line(th2,tuple(aristas[contA]),tuple(aristas[contA+1]), (0,255,0),1)
    contA+=2
"""
#aqui pinto los puntos de las esquinas que son circulos de de radio de 5 pixeles, el -1 indica que van rellenados los circulos
#point tiene la forma [fila, columna]
for point in vertices:
    cv2.circle(th2,(point[0], point[1]), 5, (255,0,0), -1)    
    cv2.waitKey(1)
    


#aqui muestro como quedo de chingon el grafo
cv2.imshow('lines',th2)
"""
las sigueitnes variables son solo una idea de como podrian llamas sus variables para el algoritmo de PRIM
"""

visitados=[]
#inicializo mi arbol
arbol=[]
contNo=0
bandVi=False
while(bandVi!=True):
    nodoI=int(input("Eliga el nodo de inicio\n"))
    for o in nodos:
        if nodos[contNo][0]==nodoI:
            visitados.append(nodos[contNo][1])
            bandVi=True
            break
        contNo+=1
           
    if(bandVi==False):
        print("No es posible iniciar de ese nodo")
bandBus=True
contBusqueda=0
while(contBusqueda!=11):    
    bandBus=BuesquedaA(visitados,aristas,nodos,arbol)
    contBusqueda+=1
print(visitados)
#y mi lista de visitados

#agrego un elemento Aleatorio de los vertices yo agrego el primero ustedes sabran cual agregan
#visitados.append(verticesConectados[0])
#aqui voy a poner la lista de posibles
#verticesNew=[]
"""
aqui deberia ir su algoritmo de prim
"""

#Aqui pinto cada una de las las lineas del arbol de color rojo en la imagen original
#recuerda opencv "cv2" maneja BGR 
cv2.imshow('final',mapa)