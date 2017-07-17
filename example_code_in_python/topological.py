"""
    topological.py
    ~~~~~~~~~~~~~~

    :copyright: (c) 2017 by C. W.
    :license: GPLv3

    Compute topological ordering of a DAG or edge-weighted DAG.
    Runs in O(E + V) time.

    % python topological.py jobs.txt "/"
    Calculus
    Linear Algebra
    Introduction to CS
    Advanced Programming
    Algorithms
    Theoretical CS
    Artificial Intelligence
    Robotics
    Machine Learning
    Neural Networks
    Databases
    Scientific Computing
    Computational Biology

"""
from digraph import Digraph
from directed_cycle import DirectedCycle
from depth_first_order import DepthFirstOrder


class Topological(object):

    def __init__(self, G):
        finder = DirectedCycle(G)

        if finder.has_cycle() is False:
            dfo = DepthFirstOrder(G)
            self.__order = dfo.reverse_post()
            self.__rank = [0] * G.V()
            for index, v in enumerate(self.__order):
                self.__rank[v] = index
        else:
            self.__order = None

    def order(self):
        return self.__order

    def has_order(self):
        return self.__order is not None

    def is_DAG(self):
        return self.has_order()

    def rank(self, v):
        self.__validate_vertex(v)
        if self.has_order():
            return self.__rank[v]
        else:
            return -1

    def __validate_vertex(self, v):
        V = len(self.__rank)
        if v < 0 or v >= V:
            raise ValueError("vertex %s is not between 0 and %s" % (
                v, V))


class SymbolGraph:
    def __init__(self, file_name, separator):
        self.__symbols = {}
        with open(file_name, 'r') as f:
            for line in f:
                tokens = line.strip().split(separator)
                for token in tokens:
                    if token not in self.__symbols:
                        self.__symbols[token] = len(self.__symbols)

        self.__keys = [0] * len(self.__symbols)
        for k, v in self.__symbols.items():
            self.__keys[v] = k

        self.__g = Digraph(len(self.__symbols))
        with open(file_name, 'r') as f:
            for line in f:
                tokens = line.strip().split(separator)
                v = self.__symbols[tokens[0]]
                for token in tokens[1:]:
                    self.__g.add_edge(v, self.__symbols[token])

    def contains(self, s):
        return s in self.__symbols

    def index_of(self, s):
        return self.__symbols[s]

    def name_of(self, v):
        return self.__keys[v]

    def digraph(self):
        return self.__g


def main():
    import sys

    txt_file = sys.argv[1]
    delimiter = sys.argv[2]

    sg = SymbolGraph(txt_file, delimiter)
    topological = Topological(sg.digraph())
    for v in topological.order():
        print(sg.name_of(v))


if __name__ == '__main__':
    main()
