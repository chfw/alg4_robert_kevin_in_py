"""
    depth_first_search.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2017 by C. W.
    :license: GPLv3

    Run depth first search on an undirected graph.
    Runs in O( E + V ) time.

    % python depth_first_search.py tinyG.txt 0
    0 1 2 3 4 5 6 
    NOT connected

    % python depth_first_search.py tinyG.txt 9
    9 10 11 12 
    NOT connected

"""  # flake8: noqa


class DepthFirstSearch(object):

    def __init__(self, G, s):
        self.__marked = [False] * G.V()
        self.__count = 0
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
            raise ValueError("vertex %s is not between 0 and %s" % (
                v, self.__number_of_vertices - 1))


def main():
    import sys
    from graph import Graph

    txt_file = sys.argv[1]
    G = Graph.from_txt(txt_file)
    s = int(sys.argv[2])
    search = DepthFirstSearch(G, s)
    message = ""
    for v in range(G.V()):
        if search.marked(v):
            message += "%s " % v
    print(message)
    if search.count() != G.V():
        print("NOT connected"),
    else:
        print("connected")


if __name__ == '__main__':
    main()
