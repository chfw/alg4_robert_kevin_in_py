"""
    graph.py
    ~~~~~~~~~~~~~~

    :copyright: (c) 2017 by C. W.
    :license: GPLv3

    A graph, implemented using an array of lists.
    Parallel edges and self-loops allowed

    % python graph.py tinyG.txt
    13 vertices, 13 edges
    0: 6 2 1 5
    1: 0
    2: 0
    3: 5 4
    4: 5 6 3
    5: 3 4 0
    6: 0 4
    7: 8
    8: 7
    9: 11 10 12
    10: 9
    11: 9 12
    12: 11 9

    % python graph.py mediumG.txt
    250 vertices, 1273 edges
    0: 225 222 211 209 204 202 191 176 163 160 149 114 97 80 68 59 58 49 44 24 15
    1: 220 203 200 194 189 164 150 130 107 72
    2: 141 110 108 86 79 51 42 18 14
    ...

"""  # flake8: noqa
from bag import Bag


class Graph(object):
    def __init__(self, V):
        if V < 0:
            raise ValueError("Number of vertices must be nonnegative")
        self.__V = V
        self.__E = 0
        self.__adj = []
        for v in range(V):
            self.__adj.append(Bag())

    @classmethod
    def from_txt(cls, txt_file):
        with open(txt_file, 'r') as graphfile:
            V = graphfile.readline().strip()
            V = int(V)
            E = graphfile.readline().strip()
            E = int(E)
            g = cls(V)
            for _ in range(E):
                v, w = map(int, graphfile.readline().split())
                g.add_edge(v, w)
        return g

    def V(self):
        return self.__V

    def E(self):
        return self.__E

    def __validate_vertex(self, v):
        if v < 0 or v > self.__V:
            raise ValueError("vertex %s is not between 0 and %s" % (
                v, self.__V - 1))

    def add_edge(self, v, w):
        self.__validate_vertex(v)
        self.__validate_vertex(w)
        self.__E += 1
        self.__adj[v].add(w)
        self.__adj[w].add(v)

    def adj(self, v):
        self.__validate_vertex(v)
        return self.__adj[v]

    def degree(self, v):
        self.__validate_vertex(v)
        return len(self.__adj[v])

    def __str__(self):
        ret = "%s vertices, %s edges\n" % (
            self.__V,
            self.__E
        )
        for index, bag in enumerate(self.__adj):
            ret += "%s: " % index
            if bag.size() > 0:
                ret += " ".join([str(x) for x in bag])
            ret += "\n"

        return ret


def main():
    import sys
    txt_file = sys.argv[1]
    G = Graph.from_txt(txt_file)
    print(G)


if __name__ == '__main__':
    main()
