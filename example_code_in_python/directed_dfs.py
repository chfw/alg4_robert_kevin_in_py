"""
    directed_dfs.py
    ~~~~~~~~~~~~~~

    :copyright: (c) 2017 by C. W.
    :license: GPLv3

    Determine single-source or multiple-source reachability
    in a digraph using depth first search
    Runs in O(E + V) time

    % python directed_dfs.py tinyDG.txt 1
    1

    % python directed_dfs.py tinyDG.txt 2
    0 1 2 3 4 5

    % python directed_dfs.py tinyDG.txt 1 2 6
    0 1 2 3 4 5 6 8 9 10 11 12

"""


class DirectedDFS(object):

    def __init__(self, G, sources):
        self.__marked = [False] * G.V()
        self.__count = 0

        for s in sources:
            self.__validate_vertex(s)
            if self.__marked[s] is False:
                self.__dfs(G, s)

    def __dfs(self, G, v):
        self.__count += 1
        self.__marked[v] = True

        for w in G.adj(v):
            if self.__marked[w] is False:
                self.__dfs(G, w)

    def marked(self, v):
        self.__validate_vertex(v)
        return self.__marked[v]

    def count(self):
        return self.__count

    def __validate_vertex(self, v):
        V = len(self.__marked)
        if v < 0 or v >= V:
            raise ValueError(
                "vertext %s is not between 0 and %s" % (v, V))

    def __validate_vertices(self, vertices):
        for v in vertices:
            self.__validate_vertex(v)


def main():
    import sys
    from bag import Bag
    from digraph import Digraph

    file_name = sys.argv[1]
    g = Digraph.from_txt(file_name)

    sources = Bag()
    for argument in sys.argv[2:]:
        s = int(argument)
        sources.add(s)

    dfs = DirectedDFS(g, sources)

    reachable = []
    for v in range(g.V()):
        if dfs.marked(v):
            reachable.append(str(v))

    print(" ".join(reachable))


if __name__ == '__main__':
    main()
