from queue import Queue

class Node:
    def __init__(self, value):
        self.value = value


class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        node = Node(value)
        self.adjacency_list[node] = []
        # returns the added node

    def add_edge(self, start_node, end_node, weight=1):
        pass

    def get_nodes(self):
        pass

    def get_neighbours(self, node):
        pass
        # collection of edges
        # including the weight

    def size(self):
        pass
        # Total numbe rof nodes in graph

    def bfs(self, start_node):
        nodes = []  # O(1)
        visited = set() # History of visited nodes # O(1)
        breadth = Queue() # O(1)
        breadth.enqueue(start_node) # O(1)
        visited.add(start_node) # O(1)
        while len(breadth)>0: # O(n)
            node = breadth.dequeue() # O(1)
            nodes.append(node) # O(1)
            for n in self.adjacency_list[node]: # O(n)
                if n not in visited: # O(1)
                    breadth.enqueue(n) # O(1)
                    visited.add(n) # O(1)
        return nodes

# O(n^2)
# start_node = n2
# nodes = [n2, n1, n3, n4]
# visited = [n2, n1, n3, n4]
# breadth = Queue()
# len(breadth) = 0 > 0
#     node n4
#     n in [n1, n3]

# return [n2, n1, n3, n4]



# Adjacency_list = {n1:[n2,n4], n2:[n1,n3], n3:[n2], n4:[n1,n3], n5:[]}


        # n1-----------n2
        #     \       /
        #      \    /
        #        \
        #       /  \
        #     /       \
        # n3  <------  n4    n5
