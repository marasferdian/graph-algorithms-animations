from graphanim.graphanim.animation import GraphAnimation
from graphanim.graphanim.utils import find_optimal_coords, random_graph
import numpy as np

highlighted_1 = (255, 0, 0)
highlighted_2 = (0, 0, 255)
unhighlighted = (127, 127, 127)

class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = list()
        self.color = unhighlighted

    def add_neighbor(self, v):
        nset = set(self.neighbors)
        if v not in nset:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):

        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))
