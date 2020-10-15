from graphanim.graphanim.animation import GraphAnimation
from graphanim.graphanim.utils import find_optimal_coords, random_graph
import numpy as np
from graph_utils import Graph, Vertex, unhighlighted, highlighted_1, highlighted_2
import heapq

labels = 'ABCDEFGHIJKLM'
labelsDict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12}
heuristic = {'A': 380, 'B': 374, 'C': 366, 'D': 329, 'E': 244, 'F': 253, 'G': 193, 'H': 176, 'I': 100, 'J': 160, 'K': 0,
             'L': 241, 'M': 242}
edges = {'AB': 71, 'AF': 151, 'BC': 75, 'CD': 118, 'CF': 140, 'DE': 111, 'EL': 70, 'LM': 75,
         'MJ': 120, 'FG': 80, 'FH': 99, 'GJ': 148, 'GI': 97, 'IJ': 138, 'IK': 101, 'HK': 211}


class InformedSearchGraph(Graph):
    def uniform_cost_search(self, start_node, target_node):
        heap = []
        dist = {}
        prev = {}
        for v in self.vertices.keys():
            dist[v] = np.inf
        dist[start_node.name] = 0
        prev[start_node.name] = -1
        heapq.heappush(heap, (0, start_node.name))
        #anim.set_node_color(labelsDict[start_node.name], color=highlighted_1)
        #anim.next_frame()
        print(dist)
        while len(heap) > 0:
            d, node = heapq.heappop(heap)
            anim.set_node_color(labelsDict[node], color=highlighted_2)
            anim.next_frame()
            if d != dist[node]:
                continue
            if node == target_node.name:
                for each in self.vertices.keys():
                    anim.set_node_color(labelsDict[each], color=unhighlighted)
                    anim.next_frame()
                anim.set_node_color(labelsDict[target_node.name], color=highlighted_2)
                anim.next_frame()
                previousNodeLabel = target_node.name
                while previousNodeLabel != -1:
                    anim.set_node_color(labelsDict[previousNodeLabel], color=highlighted_2)
                    anim.next_frame()
                    previousNodeLabel = prev[previousNodeLabel]
                return d
            for x in self.vertices[node].neighbors:
                e = self.get_edge(node, x)
                if e not in edges.keys():
                    e = self.get_edge(x, node)
                cost = d + edges[e]
                if cost < dist[x]:
                    prev[x] = node
                    anim.set_node_color(labelsDict[x], color=highlighted_1)
                    anim.next_frame()
                    dist[x] = cost
                    heapq.heappush(heap, (cost, x))
        return np.inf


graph = InformedSearchGraph()
start = Vertex('A')
target = Vertex('K')
graph.add_vertex(start)
graph.add_vertex(target)
for i in range(ord('A'), ord('N')):
    graph.add_vertex(Vertex(chr(i)))
    for edge in list(edges.keys()):
        graph.add_edge(edge[:1], edge[1:])

adj_list = []
for key in sorted(list(graph.vertices.keys())):
    edgeList = []
    for neighbor in graph.vertices[key].neighbors:
        edge = str(key) + str(neighbor)
        if edge not in edges.keys():
            edge = str(neighbor) + str(key)
        edgeList.append((labelsDict[neighbor], edges[edge]))
    adj_list.append(edgeList)

locations = find_optimal_coords(13, adj_list, verbose=True, tolerance=1e-4, max_iter=200, mutation_rate=0.4,
                               curved_edges=False, spring_mode='edges_only', node_spacing_factor=0.5)

anim = GraphAnimation(13, adj_list, locations[:, 0], locations[:, 1], labels=labels, initial_color=unhighlighted)
anim.next_frame()
print(graph.uniform_cost_search(start, target))
anim.save_gif('ucs.gif', node_radius=20, size=(800, 800), fps=1.2)
anim.save_json('ucs.json')
