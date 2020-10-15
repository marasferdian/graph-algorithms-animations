from graphanim.graphanim.animation import GraphAnimation
from graphanim.graphanim.utils import find_optimal_coords, random_graph
import numpy as np
from graph_utils import Graph, Vertex, highlighted_2, highlighted_1, unhighlighted

labels = 'ABCDEFGHIJ'
labelsDict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}


class DFSGraph(Graph):

    def _dfs(self, vertex):
        anim.set_node_color(labelsDict[vertex.name], color=highlighted_1)
        anim.next_frame()
        vertex.color = highlighted_1
        for v in vertex.neighbors:
            if self.vertices[v].color == unhighlighted:
                self._dfs(self.vertices[v])
        anim.set_node_color(labelsDict[vertex.name], color=highlighted_2)
        anim.next_frame()
        vertex.color = highlighted_2

    def _depth_lim_dfs(self, vertex, depth, maxDepth):
        if vertex.name == target.name:
            anim.set_node_color(labelsDict[vertex.name], color=highlighted_2)
            anim.next_frame()
            vertex.color = highlighted_2
            return True
        vertex.color = highlighted_1
        anim.set_node_color(labelsDict[vertex.name], color=highlighted_1)
        anim.next_frame()
        depth += 1
        if depth > maxDepth:
            depth -= 1
            vertex.color = unhighlighted
            anim.set_node_color(labelsDict[vertex.name], color=unhighlighted)
            return False
        else:
            for v in vertex.neighbors:
                if self.vertices[v].color == unhighlighted:
                    result = self._depth_lim_dfs(self.vertices[v], depth, maxDepth)
                    if result:
                        return True
                    else:
                        self.vertices[v].color = unhighlighted
                        anim.set_node_color(labelsDict[self.vertices[v].name], color=unhighlighted)

    def dfs(self, vertex):
        self._dfs(vertex)

    def depth_limited_dfs(self, source, target, maxDepth):
        depth = 0
        return self._depth_lim_dfs(source, depth, maxDepth)

    def iterative_deepening_search(self, source, target):
        depth = 0
        while not self.depth_limited_dfs(source, target, depth):
            depth += 1
        print('Found a solution at depth ' + str(depth))


graph = DFSGraph()
start = Vertex('A')
target = Vertex('H')  # for depth-limited search
graph.add_vertex(start)
graph.add_vertex(target)

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

locations = find_optimal_coords(10, adj_list, verbose=True, tolerance=1e-4, max_iter=1000, mutation_rate=0.4,
                                curved_edges=False, spring_mode='edges_only', node_spacing_factor=0.5)

anim = GraphAnimation(10, adj_list, locations[:, 0], locations[:, 1], labels=labels, initial_color=unhighlighted)
anim.next_frame()
# graph.dfs(start)
# graph.depth_limited_dfs(start, target, 3) # try depth 3 to see the algorithm at work :)
graph.iterative_deepening_search(start, target)
anim.next_frame()
# anim.save_gif('dfs.gif', node_radius=20, size=(800, 800), fps=1.2)
# anim.save_json('dfs.json')

# anim.save_gif('depth-limited.gif', node_radius=20, size=(800, 800), fps=1.2)
# anim.save_json('depth-limited.json')

anim.save_gif('iterative-deepening.gif', node_radius=20, size=(800, 800), fps=1.2)
anim.save_json('iterative-deepening.json')
