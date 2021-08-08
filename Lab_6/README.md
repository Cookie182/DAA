```python
  
from queue import Queue
import numpy as np
import time

#===================================================================================================#


class Graph:
    def __init__(self, tree, start):
        self.tree = tree
        self.start = start

    def show(self):  # to show the tree and starting node
        print(f'Start at: {self.start}')
        time.sleep(1)
        for keys, values in tree.items():
            print('Parent: {0}, Values = {1}'.format(keys, values))
            time.sleep(0.5)

    #===================================================================================================#

    def bfs(self):  # Breadth first search
        visited = {}  # store nodes already visited
        trav_turn = {}  # store turns for pre and post visiting
        travel = []  # in order traversal
        queue = Queue()

        for node in self.tree.keys():
            visited[node] = False  # by default, none are visited
            # print(visited)

        # starting with the source node
        visited[self.start] = True
        queue.put(self.start)
        while not queue.empty():
            first_q = queue.get()  # popping left-most element of queue
            travel.append(first_q)

            # to explore the adjacent ver
            for vertex in self.tree[first_q]:
                if not visited[vertex]:  # checking if vertex not already visited
                    visited[vertex] = True
                    queue.put(vertex)

        print('BFS')
        time.sleep(1)
        print('Inorder traversal (BFS) with starting point {} ='.format(
            self.start), *travel, '\n')
        time.sleep(1)
        if set(tree.keys()) == set(travel):  # check if the graph is connected
            print('The tree is connected')
        else:
            print('The tree is not connected')

    #===================================================================================================#

    def dfs(self):  # Depth first search
        global trav_turn
        global visited
        global travel
        global end_turn
        global start_turn

        trav_turn = {}  # to store the pre and print visited turn count
        visited = {}  # to store already visited nodes
        travel = []  # in order traversal
        end_turn = 1  # post visit count
        start_turn = 0  # pre visit count

        for node in self.tree.keys():  # starting values for each node
            visited[node] = False
            trav_turn[node] = [np.nan, np.nan]

        def _dfs(x):  # helper
            global end_turn

            global start_turn
            start_turn += 1

            # starting point
            visited[x] = True
            trav_turn[x][0] = start_turn
            trav_turn[x][1] = end_turn
            travel.append(x)

            # recursively calls the function until it reaches the last node of the parent node
            for y in self.tree[x]:
                if visited[y] == False:
                    _dfs(y)

            # updating turn counter
            trav_turn[x][1] = start_turn + end_turn
            end_turn += 1
        _dfs(self.start)  # recursively call helper function

        print('DFS')
        time.sleep(1)
        print('Inorder traversal (DFS) with starting point {} ='.format(
            self.start), *travel)
        time.sleep(1)
        # print the counts after checking if graph is connected
        if set(self.tree.keys()) == set(travel):
            print('\nThe tree is connected')
            print('\nPre and post visited counts:')
            for key, values in trav_turn.items():
                time.sleep(1)
                print(
                    f'For node {key}, pre visited count = {values[0]} and post visited count = {values[1]}')
        else:
            print('The tree is not connected')

    #===================================================================================================#

    def compute(self):
        self.show()  # showing the tree and starting point
        print('\n#=============================================================#\n')
        time.sleep(1)
        self.bfs()  # BFS inorder traversal and showing if tree is connected or not
        print('\n#=============================================================#\n')
        time.sleep(1)
        self.dfs()  # DFS inorder traversal, pre and post visit counts and showing if tree is connected or not
        print('\n#=============================================================#\n')


# the given graph (adjacency list format)
tree = {1: [2, 3],
        2: [1, 4],
        4: [2, 3],
        3: [1, 4, 5],
        5: [3, 6],
        6: [5]}

test = Graph(tree, 1)  # initializing tree and starting point
test.compute()
time.sleep(1)
print('Ashwin Rajesh Jawalikar, 20190802140')
```
