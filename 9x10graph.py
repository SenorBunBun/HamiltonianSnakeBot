import matplotlib.pyplot as plt
import networkx as nx

graph = nx.grid_2d_graph(10,9)
plt.figure(figsize=(5,5))
pos = {(x,y):(y,-x) for x,y in graph.nodes()}
nx.draw(graph, pos=pos,
        node_color='#1d5b75',
        with_labels=False,
        node_size=200)
plt.show()