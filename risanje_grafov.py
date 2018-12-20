import networkx as nx
import matplotlib.pyplot as plt
import numpy
import simulirano_ohlajanje
import pozresna_metoda

A=numpy.random.randint(0,2,(10,10))
G=nx.from_numpy_matrix(A)
(A,B) = simulirano_ohlajanje.simulirano_ohlajanje(A)
color_map = []
for node in G:
    if node in A:
        color_map.append('blue')
    else:
        color_map.append('green')
nx.draw(G,node_color = color_map,with_labels = True)
plt.show()

#predloga barvanja grafov na dve barvi:
""" G = nx.erdos_renyi_graph(20,0.1)
color_map = []
for node in G:
    if node <10:
        color_map.append('blue')
    else:
        color_map.append('green')
nx.draw(G,node_color = color_map,with_labels = True)
plt.show() """

