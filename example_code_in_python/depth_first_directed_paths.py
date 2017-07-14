"""
    digraph.py
    ~~~~~~~~~~~~~~

    :copyright: (c) 2017 by C. W.
    :license: GPLv3

    Determine reachability in a digraph from a given vertex using
    depth-first search.
    Runs in O(E + V) time.

    % python depth_first_directed_paths.py tinyDG.txt 3
    3 to 0:  3-5-4-2-0
    3 to 1:  3-5-4-2-0-1
    3 to 2:  3-5-4-2
    3 to 3:  3
    3 to 4:  3-5-4
    3 to 5:  3-5
    3 to 6:  not connected
    3 to 7:  not connected
    3 to 8:  not connected
    3 to 9:  not connected
    3 to 10:  not connected
    3 to 11:  not connected
    3 to 12:  not connected
"""
from stack import Stack


class DepthFirstDirectedPaths:

    def __init__(self, G, s):
        self.__marked = [False] * G.V()
        self.__edge_to = [0] * G.V()
        self.__s = s
        self.__validate_vertex(s)
        self.__dfs(G, s)

    def __dfs(self, G, v):
        self.__marked[v] = True
        for w in G.adj(v):
            if self.__marked[w] is False:
                self.__edge_to[w] = v
                self.__dfs(G, w)

    def has_path_to(self, v):
        self.__validate_vertex(v)
        return self.__marked[v]

    def path_to(self, v):
        self.__validate_vertex(v)
        if self.has_path_to(v) is False:
            return None
        path = Stack()
        x = v
        while x != self.__s:
            path.push(x)
            x = self.__edge_to[x]

        path.push(self.__s)
        return path

    def __validate_vertex(self, v):
        V = len(self.__marked)
        if (v < 0 or v >= V):
            raise ValueError(
                "vertext %s is not between 0 and %s" % (v, V))


def main():
    import sys
    from digraph import Digraph

    file_name = sys.argv[1]
    G = Digraph.from_txt(file_name)

    s = int(sys.argv[2])
    dfs = DepthFirstDirectedPaths(G, s)

    for v in range(G.V()):
        if dfs.has_path_to(v):
            content = "%s to %s:  " % (s, v)
            for x in dfs.path_to(v):
                if x == s:
                    content += str(x)
                else:
                    content += '-' + str(x)
            print(content)
        else:
            print("%s to %s:  not connected" % (s, v))


if __name__ == '__main__':
    main()
