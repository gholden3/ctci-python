# Given a directed graph, design an algorithm to find out whether there is a route between two nodes
from multiprocessing import Queue
from typing import List
import unittest

## to do : update example and test case to include a case where you should skip the node because youve already
# visited it. for example add a node after c and ask to search from a to a node that doesnt exist


class Node:
    def __init__(self, vertex, adjacentLength):
        self.adjacent = [0] * adjacentLength
        self.vertex = vertex
        self.adjacentCount = 0
        self.visited = False

    def add_adjacent(self, x):
        if self.adjacentCount < len(self.adjacent):
            self.adjacent[self.adjacentCount] = x
            self.adjacentCount += 1
        else:
            print("No more adjacent nodes can be added")

    def get_adjacent(self):
        return self.adjacent

    def get_vertex(self):
        return self.vertex


class Graph:
    def __init__(self):
        self.max_vertices = 10
        self.vertices = []
        self.vertex_data = [''] * self.max_vertices
        self.count = 0

    def add_node(self, x: Node):
        if self.count < self.max_vertices:
            # check if the node is already in the graph
            if x.vertex in self.vertex_data:
                return False
            self.vertices.append(x)
            self.vertex_data[self.count] = x.vertex
            self.count += 1
        else:
            print("Graph full")

    def get_nodes(self):
        return self.vertices


def route_between_nodes(g: Graph, start: Node, end: Node):
    if start == end:
        return True
    q = Queue(len(g.get_nodes()))
    start.visited = True
    q.put(start)
    while not q.empty():
        r: Node = q.get()
        adjacents: List[Node] = r.get_adjacent()
        for adjacent_node in adjacents:
            if not adjacent_node.visited:
                if adjacent_node.vertex == end.vertex:
                    return True
                else:
                    q.put(adjacent_node)
                adjacent_node.visited = True
    return False


def createNewGraph():
    g = Graph()

    #          >  a ---> d ----> e ---> f
    #        /   | \    |      |
    #       /   v   \   |      v
    #     i<---b    v  v      g
    #          ^ ---  c
    #                 |
    #                 v
    #                 h

    a_node = Node("a", 3)
    b_node = Node("b", 0)
    c_node = Node("c", 1)
    d_node = Node("d", 2)
    e_node = Node("e", 2)
    f_node = Node("f", 0)
    g_node = Node("g", 0)
    h_node = Node("h", 0)
    i_node = Node("i", 0)

    a_node.add_adjacent(b_node)
    a_node.add_adjacent(c_node)
    a_node.add_adjacent(d_node)
    b_node.add_adjacent(i_node)
    c_node.add_adjacent(h_node)
    c_node.add_adjacent(b_node)
    d_node.add_adjacent(e_node)
    d_node.add_adjacent(c_node)
    e_node.add_adjacent(f_node)
    e_node.add_adjacent(g_node)
    i_node.add_adjacent(a_node)

    g.add_node(a_node)
    g.add_node(b_node)
    g.add_node(c_node)
    g.add_node(d_node)
    g.add_node(e_node)
    g.add_node(f_node)
    g.add_node(g_node)
    g.add_node(h_node)
    g.add_node(i_node)

    return g


class Tests(unittest.TestCase):


    def test_route_between_nodes(self):
        g = createNewGraph()
        a_node = g.vertices[0]
        self.assertTrue(route_between_nodes(g, a_node, a_node))
        g = createNewGraph()
        a_node = g.vertices[0]
        c_node = g.vertices[2]
        path_exists = route_between_nodes(g, a_node, c_node)
        if path_exists:
            print(path_exists)
        self.assertFalse( path_exists)
        g = createNewGraph()
        b_node = g.vertices[1]
        c_node = g.vertices[2]
        self.assertFalse(route_between_nodes(g, b_node, c_node))
        g = createNewGraph()
        a_node = g.vertices[0]
        h_node = g.vertices[7]
        self.assertTrue(route_between_nodes(g,a_node, h_node))
        # self.assertFalse(route_between_nodes(self.test_graph, self.d_node, self.b_node))


if __name__ == '__main__':
    unittest.main()