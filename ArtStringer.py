# https://www.python-graph-gallery.com/321-custom-networkx-graph-appearance <- helpful

from array import array
import networkx as nx
import matplotlib.pyplot as plt

per = [0] * 200       #create an empty array with 200 slots 
for i in range(len(per)): #force the labels to show clockwise and a quarter earlier
    per[i] = abs(i - len(per)) + 50 
    if per[i] > 200: per[i] -= 200
G = nx.Graph()
G.add_nodes_from(per)
nx.draw(G, pos=nx.circular_layout(G), 
            with_labels=True, 
            node_size=0, 
            font_size=5)
plt.savefig("artGraph.eps")
plt.show() 

