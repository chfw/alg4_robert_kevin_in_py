"""
    digraph.py
    ~~~~~~~~~~~~~~

    :copyright: (c) 2017 by C. W.
    :license: GPLv3

    A graph, implemented using an array of lists.
    Parallel edges and self-loops are permitted

    % python digraph.py tinyDG.txt
    13 vertices, 22 edges
    0: 5 1 
    1: 
    2: 0 3 
    3: 5 2 
    4: 3 2 
    5: 4 
    6: 9 4 8 0 
    7: 6 9 
    8: 6 
    9: 11 10 
    10: 12 
    11: 4 12 
    12: 9 

"""  # flake8: noqa
from bag import Bag


class Digraph(object):

    def __init__(self, V):
        self.__V = V
        self.__E = 0
        self.__indgree = [0] * V
        self.__adj = [Bag() for _ in range(V)]

    def V(self):
        return self.__V

    def E(self):
        return self.__E

    def __validate_vertex(self, v):
        if (v < 0 or v >= self.__V):
            raise ValueError(
                "vertext %s is not between 0 and %s" % (v, self.__V))

    def add_edge(self, v, w):
        self.__validate_vertex(v)
        self.__validate_vertex(w)
        self.__adj[v].add(w)
        self.__indgree[w] += 1
        self.__E += 1

    def adj(self, v):
        self.__validate_vertex(v)
        return self.__adj[v]

    def out_degree(self, v):
        self.__validate_vertex(v)
        return self.__adj[v].size()

    def in_degree(self, v):
        self.__validate_vertex(v)
        return self.__indgree[v]

    def reverse(self):
        reverse = Digraph(self.__V)
        for v in range(self.__V):
            for w in self.__adj[v]:
                reverse.add_edge(w, v)
        return reverse

    def __str__(self):
        content = "%s vertices, %s edges\n" % (self.__V, self.__E)
        for v in range(self.__V):
            content += "%s: " % v
            for w in self.__adj[v]:
                content += "%s " % w
            content += "\n"
        return content

    @classmethod
    def from_txt(cls, txt_file):
        with open(txt_file, 'r') as graphfile:
            V = graphfile.readline().strip()
            V = int(V)
            E = graphfile.readline().strip()
            E = int(E)
            g = cls(V)
            for _ in range(E):
                v, w = [int(x) for x in graphfile.readline().split()]
                g.add_edge(v, w)

        return g


def main():
    import sys
    file_name = sys.argv[1]
    g = Digraph.from_txt(file_name)
    print(str(g))


if __name__ == '__main__':
    main()
