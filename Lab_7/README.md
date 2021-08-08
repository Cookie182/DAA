```python
import pandas as pd
import time
import heapq
from collections import defaultdict
import numpy as np
from matplotlib import pyplot as plt
plt.style.use('classic')


class Graph:  # class that does it all
    def __init__(self, graph):
        self.graph = graph
        self.parent = {}
        self.rank = {}

    #==================================================================#

    def prim(self, source='a'):
        """ Func to find the MST via Prim's algorithm """
        print("\n=============================")
        print("MST with Prim's Algorithm\n")

        # asking for source, getting valid input
        choice = input("Default source node = 'a', change? [Y/N]: ").lower().strip()
        if choice == 'y':
            while True:  # loop to get valid input
                source = input(
                    f"\nEnter source node {set(self.graph.keys())}: ").strip()
                # check if alpha and in graph
                if (source.isalpha()) and (source.lower() in self.graph.keys()):
                    source = source.lower()
                    break
                else:
                    print('Enter valid input from {}\n'.format(
                        list(self.graph.keys())))

        print(f"Start from = {source}")
        prim_path = defaultdict(set)  # tree path
        visited = [source]
        # automatically making the vertex from node goal node and coupling in their respective weight
        vertex = [(weight, source, goal)
                  for goal, weight in self.graph[source].items()]
        # automatically prioritize node with smallest weight
        heapq.heapify(vertex)

        while vertex:  # looping until vertex heap is empty
            # print(vertex)
            weight, start, goal = heapq.heappop(vertex)
            if goal not in visited:  # storing nodes that are visited
                visited.append(goal)
                prim_path[start].add(goal)  # adding the children of nodes
                for next, weight in self.graph[goal].items():
                    if next not in visited:  # add unvisited nodes and their weight to the heap
                        heapq.heappush(vertex, (weight, goal, next))

        # pairing start and destinations
        prim_path = list(zip(list(prim_path.keys()), list(
            prim_path[x] for x in prim_path.keys())))

        # pretty printing the result
        time.sleep(0.2)
        tot_weight = 0
        i = 1
        for keys, values in prim_path:
            time.sleep(0.5)
            values = list(values)
            print('=' * 35)
            for x in range(len(values)):
                if x == 0:
                    print("{0}. From {1} ->".format(i, keys), " -> ".join(map(str, values[x])),
                          'weight -> {0}'.format(self.graph[keys][values[x]]))
                else:
                    print("          ->".format(keys), " -> ".join(map(str, values[x])),
                          'weight -> {0}'.format(self.graph[keys][values[x]]))
                time.sleep(0.2)
            i += 1
            tot_weight += np.sum([self.graph[keys][x] for x in values])
            print("   Cummulative weight so far -> {}".format(tot_weight))
        time.sleep(0.5)
        print("\nMST total weight ->", tot_weight)

    #==================================================================#

    def find(self, v):
        """ Func to find the root of an element in a set """
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])

        return self.parent[v]

    def union(self, v, u):
        """ Func to join 2 subsets """
        first = self.find(v)  # finding the root of both nodes
        second = self.find(u)

        # find the smaller weight node
        if self.rank[first] > self.rank[second]:
            self.parent[second] = first
        else:
            self.parent[first] = second
            if self.rank[first] == self.rank[second]:
                self.rank[second] += 1

    def kruskal(self):
        """ Func to construct MST using Kruskal's algorithm """
        for v in self.graph.keys():
            self.parent[v] = v
            self.rank[v] = 0

        vertexs = []  # storing vertices
        path = []  # storing path result

        for out_key in self.graph.keys():  # iterating through children of nodes
            for in_key, in_key_weight in self.graph[out_key].items():
                vertexs.append((in_key_weight, out_key, in_key))

        vertexs.sort()

        for vertex in vertexs:  # to find path with no cycles
            weight, v, u = vertex

            if self.find(v) != self.find(u):  # closed loop checker
                self.union(v, u)
                path.append(vertex)

        i = 0
        print("=============================")
        print("MST with Kruskal algorithm\n")
        for x in range(len(path)):
            i += 1
            print(f"{i}. {path[x][1]} <--> {path[x][2]} weight = {path[x][0]}")
            time.sleep(0.2)
        time.sleep(0.2)
        print(f"\nTotal Weight -> {np.sum([x[0] for x in path])}")
        time.sleep(0.2)

        # storing the points for the nodes
        points = [[1, 2],
                  [2, 3], [2, 1],
                  [3, 2],
                  [4, 1], [4, 3],
                  [5, 1], [5, 3],
                  [6, 2]]

        # appointing points to the appropriate node
        a, b, h, i, g, c, f, d, e = map(tuple, points)
        nodes = ['a', 'b', 'h', 'i', 'g', 'c', 'f', 'd', 'e']  # node tags

        # creating a custom points version of the graph (no string tags, instead just the points)
        graph_nodes = {a: {b: 4, h: 8},
                       b: {a: 4, h: 11, c: 8},
                       h: {a: 8, b: 11, i: 7, g: 1},
                       i: {h: 7, g: 6, c: 2},
                       g: {h: 1, i: 6, f: 2},
                       c: {b: 8, i: 2, f: 4, d: 7},
                       f: {g: 2, c: 4, d: 14, e: 10},
                       d: {c: 7, f: 14, e: 6},
                       e: {d: 6, f: 10}}

        def tag(x, y, tag, color='white'):
            """ Func to plot the nodes and the necessary tags for the graph """
            plt.text(x, y, tag, fontdict={'color': color, 'size': 20},
                     horizontalalignment='center', verticalalignment='center')

        fig = plt.figure(frameon=False, figsize=(12, 9))

        # Unmodified graph
        fig.add_subplot(1, 2, 1)
        for z in range(len(nodes)):
            x = list(graph_nodes.keys())[z]
            for y in graph_nodes[x]:
                plt.scatter([x[0], y[0]], [x[1], y[1]], s=2400,
                            c='black', zorder=2, edgecolor='blue', linewidth=5)
                plt.plot([x[0], y[0]], [x[1], y[1]],
                         c='black', zorder=1, linewidth=20)
                plt.plot([x[0], y[0]], [x[1], y[1]],
                         c='red', zorder=1, linewidth=7)
            plt.text(points[z][0], points[z][1], nodes[z],
                     fontdict={'color': 'white', 'family': 'Comic Sans MS', 'size': 25}, horizontalalignment='center', verticalalignment='center')

        # weight tags
        tag(1.4, 1.4, 8, 'black')
        tag(1.4, 2.65, 4, 'black')
        tag(1.8, 2, 11, 'black')
        tag(3, 1.1, 1, 'black')
        tag(2.7, 1.5, 7, 'black')
        tag(3.3, 1.5, 6, 'black')
        tag(3, 2.9, 8, 'black')
        tag(3.3, 2.5, 2, 'black')
        tag(4.5, 2.9, 7, 'black')
        tag(4.8, 2, 14, 'black')
        tag(4.3, 2, 4, 'black')
        tag(5.3, 2.5, 6, 'black')
        tag(4.5, 1.1, 2, 'black')
        tag(5.3, 1.5, 10, 'black')

        plt.gca().set_title('Graph', fontsize=15)
        plt.gca().axes.get_xaxis().set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)
        plt.tight_layout()

        # MST graph with Kruskal algorithm
        fig.add_subplot(1, 2, 2)
        for z in range(len(nodes)):
            x = list(graph_nodes.keys())[z]
            for y in graph_nodes[x]:
                plt.scatter([x[0], y[0]], [x[1], y[1]], s=2400,
                            c='black', zorder=3, edgecolor='blue', linewidth=5)
                plt.plot([x[0], y[0]], [x[1], y[1]], c='red',
                         zorder=1, linewidth=20, alpha=0.1)
            plt.text(points[z][0], points[z][1], nodes[z],
                     fontdict={'color': 'white', 'family': 'Comic Sans MS', 'size': 25}, horizontalalignment='center', verticalalignment='center')

        for x in range(len(path)):
            edge = (nodes.index(path[x][1]), nodes.index(path[x][2]))
            plt.plot([points[edge[0]][0], points[edge[1]][0]], [points[edge[0]][1], points[edge[1]][1]], zorder=2,
                     c='black', linewidth=20, alpha=1)
            plt.plot([points[edge[0]][0], points[edge[1]][0]], [points[edge[0]][1], points[edge[1]][1]], zorder=2,
                     c='red', linewidth=7, alpha=1)

        # weight tags
        tag(1.4, 1.4, 8, 'black')
        tag(1.4, 2.65, 4, 'black')
        tag(3, 1.1, 1, 'black')
        tag(3.3, 2.5, 2, 'black')
        tag(4.5, 2.9, 7, 'black')
        tag(4.3, 2, 4, 'black')
        tag(5.3, 2.5, 6, 'black')
        tag(4.5, 1.1, 2, 'black')

        plt.gca().set_title('MST via Kruskal Algorithm, Total Weight -> {}'.format(
            np.sum([x[0] for x in path])), fontsize=15)
        plt.gca().axes.get_xaxis().set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)
        plt.tight_layout()
        fig.canvas.set_window_title(
            'Finding MST using Kruskal algorithm on given graph')
        plt.show()

        return ''

    #==================================================================#

    def show_edges(self):
        """ Func to pretty print out the nodes and it's children along with the each of their weight """
        print('Graph:')
        i = 0
        for key in list(self.graph.keys()):
            sub_keys = list(self.graph[key].keys())
            i = i + 1
            for sub_key in sub_keys:
                if sub_key == sub_keys[0]:
                    print(
                        '-' * len(f"{i}. From {key} <--> {sub_key}, weight = {self.graph[key][sub_key]}"))
                    print(
                        f'{i}. From {key} <--> {sub_key}, weight = {self.graph[key][sub_key]}')
                    time.sleep(0.2)
                else:
                    print(
                        f"{' ' * len(f'{i}. From {key}')} <--> {sub_key}, weight = {self.graph[key][sub_key]}")
                    time.sleep(0.2)
        print(
            '-' * len(f"{i}. From {key} <--> {sub_key}, weight = {self.graph[key][sub_key]}"))

        # storing the points for the nodes
        points = [[1, 2],
                  [2, 3], [2, 1],
                  [3, 2],
                  [4, 1], [4, 3],
                  [5, 1], [5, 3],
                  [6, 2]]

        # appointing points to the appropriate node
        a, b, h, i, g, c, f, d, e = map(tuple, points)
        nodes = ['a', 'b', 'h', 'i', 'g', 'c', 'f', 'd', 'e']  # node tags

        # creating a custom points version of the graph (no string tags, instead just the points)
        graph_nodes = {a: {b: 4, h: 8},
                       b: {a: 4, h: 11, c: 8},
                       h: {a: 8, b: 11, i: 7, g: 1},
                       i: {h: 7, g: 6, c: 2},
                       g: {h: 1, i: 6, f: 2},
                       c: {b: 8, i: 2, f: 4, d: 7},
                       f: {g: 2, c: 4, d: 14, e: 10},
                       d: {c: 7, f: 14, e: 6},
                       e: {d: 6, f: 10}}

        def tag(x, y, tag, color='white'):
            """ Func to plot the nodes and the necessary tags for the graph """
            plt.text(x, y, tag, fontdict={'color': color, 'size': 20},
                     horizontalalignment='center', verticalalignment='center')

        fig = plt.figure(frameon=False, figsize=(12, 9))

        for z in range(len(nodes)):
            x = list(graph_nodes.keys())[z]
            for y in graph_nodes[x]:
                plt.scatter([x[0], y[0]], [x[1], y[1]], s=2400,
                            c='black', zorder=2, edgecolor='blue', linewidth=5)
                plt.plot([x[0], y[0]], [x[1], y[1]],
                         c='black', zorder=1, linewidth=20)
                plt.plot([x[0], y[0]], [x[1], y[1]],
                         c='red', zorder=1, linewidth=7)
            plt.text(points[z][0], points[z][1], nodes[z],
                     fontdict={'color': 'white', 'family': 'Comic Sans MS', 'size': 25}, horizontalalignment='center', verticalalignment='center')

        # weight tags
        tag(1.4, 1.4, 8, 'black')
        tag(1.4, 2.65, 4, 'black')
        tag(1.8, 2, 11, 'black')
        tag(3, 1.1, 1, 'black')
        tag(2.7, 1.5, 7, 'black')
        tag(3.3, 1.5, 6, 'black')
        tag(3, 2.9, 8, 'black')
        tag(3.3, 2.5, 2, 'black')
        tag(4.5, 2.9, 7, 'black')
        tag(4.8, 2, 14, 'black')
        tag(4.3, 2, 4, 'black')
        tag(5.3, 2.5, 6, 'black')
        tag(4.5, 1.1, 2, 'black')
        tag(5.3, 1.5, 10, 'black')

        plt.gca().set_title('Graph')
        plt.gca().axes.get_xaxis().set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)
        plt.tight_layout()
        fig.canvas.set_window_title('Given graph')
        plt.show()

        time.sleep(0.5)

    #==================================================================#

    def dijkstra_allpaths(self):
        """ Func to repeat the main shortest path finder function to reach all possible ends of the graph from the source node """
        print("\n=============================\nDijkstra's algorithm")

        start = 'a'
        choice = input("Default source = 'a', change? [Y/N]: ").strip()
        if choice.lower() == 'y':
            while True:  # loop to get valid input
                start = input(
                    f"\nEnter source node {set(self.graph.keys())}: ").strip()
                # check if alpha and in graph
                if (start.isalpha()) and (start.lower() in self.graph.keys()):
                    start = start.lower()
                    break
                else:
                    print('Enter valid input from {}\n'.format(
                        list(self.graph.keys())))

        paths = []
        path_times = []
        end_path = []
        path_weight = []
        print("=============================")
        # iterate through each node set as destination (other than starting node)
        for x in self.graph.keys() - start:
            self.dijkstra_path(self.graph.copy(), end=x, start=start)
            print("=============================")
            time.sleep(0.2)
            paths.append(' -> '.join(map(str, path)))
            path_times.append(path_time)
            end_path.append(x)
            path_weight.append(s_dist[x])

        print("\nDijkstra paths from source to all nodes in a graph:-\n")
        df = pd.DataFrame(list(zip(paths, path_weight, path_times)), columns=['Path', 'Weight', 'Time (s)'],
                          index=[[start] * len(path_times), end_path]).sort_values('Weight')
        df.index.set_names(['Start', 'End'], inplace=True)
        print(df)

    def dijkstra_path(self, graph, end, start):
        """ Func to find the shortest path from a specified source and end node """
        tic = time.time()

        # showing the path
        print(f"Starting from {start} to {end}")

        global s_dist
        s_dist = {}  # constantly updating weight
        prev = {}  # store the path of shortest weight
        unseen = graph  # to make sure every node gets seen while iterating
        global path
        path = []  # store end shortest path
        for node in unseen:
            s_dist[node] = float('inf')  # initial value
        s_dist[start] = 0  # start node starting with 0

        # greedy algorithm
        while unseen:  # loop until unseen dict is empty
            min = None
            for node in unseen:
                if min is None:  # base case
                    min = node
                elif s_dist[node] < s_dist[min]:
                    min = node

            for child, weight in graph[min].items():  # checking child nodes
                if weight + s_dist[min] < s_dist[child]:
                    # accumulatively adds weight from start to end node
                    s_dist[child] = weight + s_dist[min]
                    # saves the path of the accumulatively added weight
                    prev[child] = min
            unseen.pop(min)

        curr = end
        while curr != start:  # to read the path from goal to start
            path.insert(0, curr)
            curr = prev[curr]  # keep storing previous nodes in shortest path
        path.insert(0, start)
        print('\nLeast cumulative weight -> {}'.format(s_dist[end]))
        time.sleep(0.2)
        print("Path: from", ' -> '.join(map(str, path)))
        time.sleep(0.2)
        toc = time.time()
        global path_time
        path_time = np.round(toc - tic, 3)
        print(f"Time: {path_time}s")

    #==================================================================#

    def show_results(self):
        """ Func to show all the results for each question """
        self.show_edges()
        self.prim()
        self.kruskal()
        self.dijkstra_allpaths()
        time.sleep(1)
        return '\nAshwin Rajesh Jawalikar, 20190802140\nTo Dr. Saif and Ms. Vijaylaxmi -> Thank you for an awesome semester of coding!'


graph = {'a': {'b': 4, 'h': 8},
         'b': {'a': 4, 'h': 11, 'c': 8},
         'h': {'a': 8, 'b': 11, 'i': 7, 'g': 1},
         'i': {'h': 7, 'g': 6, 'c': 2},
         'g': {'h': 1, 'i': 6, 'f': 2},
         'c': {'b': 8, 'i': 2, 'f': 4, 'd': 7},
         'f': {'g': 2, 'c': 4, 'd': 14, 'e': 10},
         'd': {'c': 7, 'f': 14, 'e': 6},
         'e': {'d': 6, 'f': 10}}
lab = Graph(graph)
print(lab.show_results())
```
