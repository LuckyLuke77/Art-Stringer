# https://www.python-graph-gallery.com/321-custom-networkx-graph-appearance <- helpful links
# https://makingmathvisible.com/String-Rings/String-Rings.html

from array import array
import networkx as nx
import matplotlib.pyplot as plt


def ToFormat(num, numOfPins = 100):
    if num > numOfPins: num -= numOfPins
    return num

summOfPins = 100
pins = [0] * summOfPins       # create an empty array with 200 slots 
conns = []                    # create an enpty array that will be used to store the connections
for i in range(len(pins)):              # force the labels to show clockwise and a quarter earlier
    pins[i] = int(abs(i - len(pins)) + summOfPins / 4) 
    if pins[i] > summOfPins: pins[i] -= summOfPins
for i in range(99):
    conns.append((ToFormat(i + 1), ToFormat(i + 41)))
G = nx.Graph()
G.add_nodes_from(pins)
G.add_edges_from(conns)
nx.draw(G, pos=nx.circular_layout(G), 
            with_labels=True, 
            node_size=0, 
            font_size=5,
            width=0.5,
            alpha=0.5)
plt.savefig("artGraph.eps")
plt.show() 

