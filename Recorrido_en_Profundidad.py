# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 15:54:14 2020
@author: dell
"""

import networkx as nx
import matplotlib.pyplot as plt
def recorrido_en_profundidad(grafo1):
    pila=[]
    lista=[]
    band=0
    pila.append(grafo1['A'][1])
    while(len(pila)!=0):
            actual=pila.pop()
            l=0
            for i in lista:
                if actual==lista[l]:
                   band=1
            l+=1
            if band==0:
                l=0
                o=0
                lista.append(actual)
                print(lista)
                for i in grafo1[actual]:
                    band2=0
                    o=0
                    for j in lista:
                          if grafo1[actual][l]==lista[o]:
                              band2=1
                          o+=1
                    if band2==0:
                        pila.append(grafo1[actual][l])
                    l+=1
                    #print(pila)
def recorrido_en_anchura(grafo):
    cola=[]
    lista1=[]
    band=0
    
    visitados=[]
    cola.append(grafo['A'][1])
    visitados.append(grafo['A'][1])
    print(visitados)
    while(len(cola)!=0):
        actual=cola.pop(0)
        lista=[]
        lista1=[]
        for i in grafo[actual]:
            lista.append(ord(i))
        lista.sort()
        for i in lista:
            lista1.append(chr(i))
        for i in lista1:
            band=i in visitados
            if band==False:
                visitados.append(i)
                print(visitados)
                cola.append(i)
       # print(cola) 
grafod={
       'A':[('L'),('Y'),('S')],
       'Y':[('A'),('X')],
       'X':['F'],
       'S':[('G'),('D')],
       'D':[('I')],
       'F':[],
       'G':[('H')],
       'L':[],
       'I':[],
       'H':[]
       }
grafo1={'A':[('J'),('Z'),('L')],
        'Z':[('C'),('A')],
        'C':[('F'),('E')],
        'D':[('I')],
        'E':[('D')],
        'L':[('R')],
        'R':[],
        'J':[],
        'I':[],
        'F':[]
        }                    
grafo={'A':[('H'),('B')],
       'B':[('G'),('A'),('C')],
       'C':[('F'),('E')],
       'D':[('I')],
       'E':['D','F'],
       'F':['C'],
       'G':[('H')],
       'H':[('A')],
       'I':[('J')],
       'J':[('I')]
       }
G=nx.DiGraph()
G.add_nodes_from(grafod)
G.add_edge('Y','X')
G.add_edge('X','F')
G.add_edge('Y','A')
G.add_edge('A','L')
G.add_edge('A','S')
G.add_edge('S','G')
G.add_edge('S','D')
G.add_edge('G','H')
G.add_edge('D','I')


"""
G.add_nodes_from(grafo1)
G.add_edge('Z','C')
G.add_edge('Z','A')
G.add_edge('C','F')
G.add_edge('C','E')
G.add_edge('E','D')
G.add_edge('D','I')
G.add_edge('Z','C')
G.add_edge('A','J')
G.add_edge('A','L')
G.add_edge('L','R')
"""

G.add_node('B')
G.add_node('A')
G.add_node('G')
G.add_node('C')
G.add_node('H')
G.add_node('E')
G.add_node('D')
G.add_node('F')
G.add_node('I')
G.add_node('J')

G.add_edge('B','A')
G.add_edge('B','G')
G.add_edge('B','C')
G.add_edge('A','H')
G.add_edge('G','H')
G.add_edge('C','E')
G.add_edge('C','F')
G.add_edge('E','F')
G.add_edge('E','D')
G.add_edge('D','I')
G.add_edge('I','F')
G.add_edge('I','J')



nx.draw_planar(G,with_labels=True,node_size=200,node_color='r')
#nx.draw_random(G,with_labels=True,node_size=200,node_color='r')
nx.draw_networkx
plt.show()

print('RECORRIDO EN ANCHURA 2')
recorrido_en_anchura(grafo1)

"""
lista=[]
lista1=[]
#lista=[8,2,1,34,5,6,5]

for i in grafo['B']:
    lista.append(ord(i))
lista.sort()
for i in lista:
    lista1.append(chr(i))
print(grafo['B'])    
print(lista1)
"""

"""
lista=['G','B,','L']
l=0
for i in grafo['B']:
        band2=0
        for j in lista:
              if (grafo['B'][l]==lista[j]):
                 print(grafo['B'][l])
        l+=1
l=0
o=0
for i in grafo['B']:
    #print(grafo['B'][l])
    o=0
    for j in lista:
        if (grafo['B'][l]==lista[o]):
              print(grafo['B'][l])
        o+=1
    l+=1
"""

    
