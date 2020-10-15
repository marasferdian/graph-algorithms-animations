# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
from heapq import heappop, heappush
from graphanim.graphanim.animation import GraphAnimation
from graphanim.graphanim.utils import find_optimal_coords, random_graph


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 10
    adj_list = random_graph(n, 12)
    labels = 'ABCDEFGHIJ'
    labelsDict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}

    locations = find_optimal_coords(n, adj_list, verbose=True, tolerance=1e-4, max_iter=1000, mutation_rate=0.4,
                                    curved_edges=False, spring_mode='edges_only', node_spacing_factor=0.5)
    highlighted_1 = (255, 0, 0)
    highlighted_2 = (0, 0, 255)
    unhighlighted = (127, 127, 127)
    print(adj_list)
    anim = GraphAnimation(n, adj_list, locations[:, 0], locations[:, 1], labels=labels, initial_color=unhighlighted)
    anim.next_frame()
    anim.next_frame()
    rand = np.random.randint(100000000)
    # anim.save_gif('dijkstra%d.gif' % rand, node_radius=20, size=(800, 800), fps=1.2)
    # anim.save_json('dijkstra%d.json' % rand)
