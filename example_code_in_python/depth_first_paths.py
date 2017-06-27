"""
    depth_first_paths.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2017 by C. W.

    Run depth first search on an undirected graph.
    Runs in O( E + V ) time.

    % python graph.py tinyCG.txt
    6 vertices, 8 edges
    0: 2 1 5
    1: 0 2
    2: 0 1 3 4
    3: 5 4 2
    4: 3 2
    5: 3 0
  
    % python depth_first_paths.py tinyCG.txt 0
    0 to 0:  0
    0 to 1:  0-2-1
    0 to 2:  0-2
    0 to 3:  0-2-3
    0 to 4:  0-2-3-4
    0 to 5:  0-2-3-5

"""  # flake8: noqa


class DepthFirstPaths(object):

    def __init__(self, G, s):
        self.__marked = [False] * G.V()
        self.__edge_to = [-1] * G.V()
        self.__count = 0
        self.__s = s
        self.__dfs(G, s)

    def __dfs(self, G, v):
        self.__marked[v] = True
        for w in G.adj(v):
            if self.__marked[w] is False:
                self.__edge_to[w] = v
                self.__dfs(G, w)

    def has_path_to(self, v):
        return self.__marked[v]

    def path_to(self, v):
        self.__validate_vertex(v)
        if self.has_path_to(v) is False:
            return None
        path = []
        x = v
        while x != self.__s:
            path.insert(0, x)
            x = self.__edge_to[x]
        path.insert(0, self.__s)
        return path

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
    dfs = DepthFirstPaths(G, s)
    message = ""
    for v in range(G.V()):
        if dfs.has_path_to(v):
            message = "%s to %s:  " % (s, v)
            message += "-".join([str(x) for x in dfs.path_to(v)])
        else:
            message("%s to %s: not connected" % (s, v))
        print(message)


if __name__ == '__main__':
    main()
