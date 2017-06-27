"""
    cc.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2017 by C. W.
    :license: GPLv3

    Compute connected components using depth first searc
    Runs in O( E + V ) time.

    % python cc.py tinyG.txt
    3 components
    0 1 2 3 4 5 6
    7 8
    9 10 11 12
  
    % python cc mediumG.txt 
    1 components
    0 1 2 3 4 5 6 7 8 9 10 ...

"""  # flake8: noqa


class CC(object):
    def __init__(self, G):
        self.__marked = [False] * G.V()
        self.__id = [0] * G.V()
        self.__size = [0] * G.V()
        self.__count = 0
        for v in range(G.V()):
            if self.__marked[v] is False:
                self.__dfs(G, v)
                self.__count += 1

    def __dfs(self, G, v):
        self.__marked[v] = True
        self.__id[v] = self.__count
        self.__size[self.__count] += 1
        for w in G.adj(v):
            if self.__marked[w] is False:
                self.__dfs(G, w)

    def connected(self, v, w):
        self.__validate_vertex(v)
        self.__validate_vertex(w)
        return self.__id[v] == self.__id[w]

    def id(self, v):
        self.__validate_vertex(v)
        return self.__id[v]

    def count(self):
        return self.__count

    def size(self, v):
        self.__validate_vertex(v)
        return self.__size[self.__id[v]]

    def __validate_vertex(self, v):
        V = len(self.__marked)
        if v < 0 or v >= V:
            raise ValueError("vertex %s is not between 0 and %s" % (
                v, self.__number_of_vertices - 1))


def main():
    import sys
    from graph import Graph
    from collections import defaultdict
    
    txt_file = sys.argv[1]
    G = Graph.from_txt(txt_file)
    cc = CC(G)

    m = cc.count()
    print("%s components" % m)

    components = defaultdict(list)
    for v in range(G.V()):
        components[cc.id(v)].append(v)

    for sub in components.values():
        print ' '.join([str(x) for x in sub])


if __name__ == '__main__':
    main()
