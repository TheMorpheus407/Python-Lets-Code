import networkx as nx

G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from([
    (4, {"color": "green"}),
    (5, {"color": "red"})
])

H = nx.Graph()
H.add_node(6)
H.add_node(7)
H.add_edge(6, 7)
G.add_nodes_from(H)

G.add_edge(1, 2)
G.add_edges_from([(2, 3), (1, 3)])
G.add_edges_from(H.edges)
G.add_edges_from([(3, 6), (4, 6), (5, 4)])

I = nx.Graph()
I.add_weighted_edges_from([(1, 2, 0.9123), (1, 3, 0.5), (2, 4, 0.25), (3, 4, 0.5)])
for (u,v,w) in I.edges.data("weight"):
    print(w)

print(nx.shortest_path(I, 1, 4, "weight"))
