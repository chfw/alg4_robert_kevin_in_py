"""
    symbol_graph.py
    ~~~~~~~~~~~~~~

    :copyright: (c) 2017 by C. W.
    :license: GPLv3

    A graph, implemented using an array of lists.
    Parallel edges and self-loops allowed

    % python symbol_graph routes.txt " " # interactive
    JFK
       ORD
       ATL
       MCO
    LAX
       LAS
       PHX

    Please note the order is reversed.

"""
from graph import Graph


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

        self.__g = Graph(len(self.__symbols))
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

    def G(self):
        return self.__g


def main():
    import sys
    file_name = sys.argv[1]
    delimiter = sys.argv[2]
    sg = SymbolGraph(file_name, delimiter)
    g = sg.G()
    line = user_input().strip()
    while line != '':
        for v in g.adj(sg.index_of(line)):
            print('   ' + sg.name_of(v))
        line = user_input()


def user_input():
    try:
        return raw_input()  # flake8: noqa
    except:
        return input()


if __name__ == '__main__':
    main()
