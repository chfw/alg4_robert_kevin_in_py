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


def main():
    import sys
    from symbol_digraph import SymbolDigraph

    txt_file = sys.argv[1]
    delimiter = sys.argv[2]

    sg = SymbolDigraph(txt_file, delimiter)
    topological = Topological(sg.digraph())
    for v in topological.order():
        print(sg.name_of(v))


if __name__ == '__main__':
    main()
