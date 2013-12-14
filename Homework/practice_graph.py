import networkx as nx
G=nx.Graph()
import matplotlib.pyplot as plt

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)

G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(2,3)
G.add_edge(2,4)
G.add_edge(3,4)
G.add_edge(3,5)
G.add_edge(3,6)
G.add_edge(5,6)

nx.draw(G)
plt.show()