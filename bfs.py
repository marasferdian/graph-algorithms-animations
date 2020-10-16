import numpy as np
from graphanim.graphanim.animation import GraphAnimation
from graphanim.graphanim.utils import find_optimal_coords, random_graph
from graph_utils import Vertex, Graph, highlighted_1, highlighted_2, unhighlighted

labels = 'ABCDEFGHIJ'
labelsDict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}


class BFSGraph(Graph):
    def breadth_first_search(self, vertex):
        queue = list()
        anim.set_node_color(labelsDict[vertex.name], color=highlighted_2)
        anim.next_frame()
        for v in vertex.neighbors:
            queue.append(v)
            anim.set_node_color(labelsDict[v], color=highlighted_1)
            anim.next_frame()
            vertex.color = highlighted_1

        while len(queue) > 0:
            u = queue.pop(0)
            node_u = self.vertices[u]
            anim.set_node_color(labelsDict[node_u.name], color=highlighted_2)
            anim.next_frame()
            node_u.color = highlighted_2

            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if node_v.color == unhighlighted:
                    queue.append(v)
                    anim.set_node_color(labelsDict[node_v.name], color=highlighted_1)
                    anim.next_frame()


graph = BFSGraph()
start = Vertex('A')
graph.add_vertex(start)

for i in range(ord('A'), ord('K')):
    graph.add_vertex(Vertex(chr(i)))
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    graph.add_edge(edge[:1], edge[1:])

adj_list = []
for key in sorted(list(graph.vertices.keys())):
    edges = []
    for neighbor in graph.vertices[key].neighbors:
        edges.append((labelsDict[neighbor], 1))
    adj_list.append(edges)

locations = find_optimal_coords(10, adj_list, verbose=True, tolerance=1e-4, max_iter=200, mutation_rate=0.4,
                                curved_edges=False, spring_mode='edges_only', node_spacing_factor=0.5)

anim = GraphAnimation(10, adj_list, locations[:, 0], locations[:, 1], labels=labels, initial_color=unhighlighted)
anim.next_frame()

graph.breadth_first_search(start)
anim.next_frame()

anim.save_gif('bfs.gif', node_radius=20, size=(800, 800), fps=1.2)
anim.save_json('bfs.json')
