import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

# Creating a Graph 
G = nx.Graph() # Right now G is empty

G.add_node(1)


# You can also add a list of nodes by passing a list argument
G.add_nodes_from([2,3,4,5,6])


# Add edges 
G.add_edge(1,2)
G.add_edge(2,2)
G.add_edge(3,4)
G.add_edge(2,3)
G.add_edge(3,5)
G.add_edge(2,6)
G.add_edge(1,6)
G.add_edge(4,6)

e = (2,3)
G.add_edge(*e) # * unpacks the tuple
G.add_edges_from([(1,2), (1,3)]) # Just like nodes we can add edges from a list


# print(G) # displays the nodes and edges of the graph
# nx.draw(G, with_labels=True) # draw the network with labels
# nx.draw_networkx(G) # draw the network
# nx.draw_circular(G) # draw the network in a circular layout
# nx.draw_random(G) # draw the network in a random layout
# nx.draw_spring(G) # draw the network in a spring layout


# pos = {
#     1: (-0.1276, 51.5072),  # longitude, latitude
#     2: (-0.1180, 51.5090),
# }

# nx.draw(G, pos=pos, with_labels=True)


# plt.show()  # display the plot



import pandas as pd 
import numpy as np

df = pd.read_csv('flights.csv')

# print(df.head())


flight_graph = nx.from_pandas_edgelist(
    df,
    source="origin",
    target="dest",
    edge_attr=True,
)

# print(len(list(df['origin'].unique()) + list(df['dest'].unique())))

# print(list(flight_graph.nodes()))
# print(list(flight_graph.edges()))
# nx.draw_networkx(flight_graph, with_labels=True)
# nx.draw_circular(flight_graph, with_labels=True)
# nx.draw_spring(flight_graph, with_labels=True)

# plt.show()

cc = nx.algorithms.closeness_centrality(flight_graph) 
# print({k: v for k, v in sorted(cc.items(), key=lambda item: item[1])})
# print({k: v for k, v in sorted(cc.items(), key=lambda item: item[1], reverse=True)})

dc = nx.algorithms.degree_centrality(flight_graph)
# print({k: v for k, v in sorted(dc.items(), key=lambda item: item[1])})

bc = nx.algorithms.betweenness_centrality(flight_graph) 
# print({k: v for k, v in sorted(bc.items(), key=lambda item: item[1])})

# Average edge density of the Graphs
# print(nx.density(flight_graph))

# Average shortest path length for ALL paths in the Graph
# print(nx.average_shortest_path_length(flight_graph))

# Find all the paths available
# for path in nx.all_simple_paths(flight_graph, source='JAX', target='DFW'):
#     print(path)

# Dijkstra path from JAX to DFW.
# You can read more in-depth on how dijkstra works from: 
# https://courses.csail.mit.edu/6.006/fall11/lectures/lecture16.pdf
# dijpath = nx.dijkstra_path(flight_graph, source='JAX', target='DFW')
# print(dijpath)

# Find the dijkstra path weighted by airtime (approximate case)
# shortpath = nx.dijkstra_path(flight_graph, source='JAX', target='DFW', weight='air_time')
# print(shortpath)
