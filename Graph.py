import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()
G.add_node(0, pos=(0.0, 0.75))
G.add_node(1, pos=(0.5, 0.25))
G.add_node(2, pos=(0.375, -0.5))
G.add_node(3, pos=(-0.375, -0.5))
G.add_node(4, pos=(-0.50, 0.25))

G.add_edges_from([(2, 1)], weight=1)
G.add_edges_from([(0, 4), (1, 2), (2, 3)], weight=2)
G.add_edges_from([(0, 2)], weight=3)
G.add_edges_from([(4, 3)], weight=4)
G.add_edges_from([(0, 1)], weight=5)
G.add_edges_from([(4, 1), (1, 3)], weight=6)
G.add_edges_from([(4, 2)], weight=10)

pos = nx.get_node_attributes(G, 'pos')

multiple_edges = [edge for edge in G.edges() if reversed(edge) in G.edges()]
straight_edges = list(set(G.edges()) - set(multiple_edges))
edge_labels = nx.get_edge_attributes(G, 'weight')
edge_colors = ['black' for edge in G.edges()]

fig, ax = plt.subplots()

nx.draw_networkx_nodes(G, pos, ax=ax)
nx.draw_networkx_labels(G, pos, ax=ax)
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=straight_edges)
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=multiple_edges, connectionstyle=f'arc3, rad = {0.25}')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.25, font_size=9, rotate=False)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)


print("There is no path from Node 4 to Node 0.")
print("The length of the shortest path from Node 4 to Node 1: ",
      nx.dijkstra_path_length(G, source=4, target=1, weight='weight'))
print("The length of the shortest path from Node 4 to Node 2: ",
      nx.dijkstra_path_length(G, source=4, target=2, weight='weight'))
print("The length of the shortest path from Node 4 to Node 3: ",
      nx.dijkstra_path_length(G, source=4, target=3, weight='weight'))
plt.show()
