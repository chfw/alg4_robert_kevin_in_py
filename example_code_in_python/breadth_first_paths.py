"""
    breadth_first_paths.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2017 C. W.

    Run breadth first search on an undirected graph.
    Runs in O( E + V ) time

    % python graph.py tinyCG.txt
    6 vertices, 8 edges
    0: 2 1 5
    1: 0 2
    2: 0 1 3 4
    3: 5 4 2
    4: 3 2
    5: 3 0

    % python breadth_first_paths.py tinyCG.txt 0
    0 to 0 (0):  0
    0 to 1 (1):  0-1
    0 to 2 (1):  0-2
    0 to 3 (2):  0-2-3
    0 to 4 (2):  0-2-4
    0 to 5 (1):  0-5

    largeG.txt test is not included here. Please try it on your own

""" #flake8: noqa
from collections import deque


class BreadthFirstPaths(object):

    def __init__(self, G, s):
        self.__marked = [False] * G.V()
        self.__dist_to = [float('inf')] * G.V()
        self.__edge_to = [0] * G.V()
        self.__validate_vertex(s)
        self.__bfs(G, s)

    def __bfs(self, G, s):
        queue = deque()

        if isinstance(s, list) is False:
            s = [s]
        for single_s in s:
            self.__dist_to[single_s] = 0
            self.__marked[single_s] = True
            queue.append(single_s)

        while(len(queue) != 0):
            v = queue.popleft()
            for w in G.adj(v):
                if self.__marked[w]:
                    continue
                self.__edge_to[w] = v
                self.__dist_to[w] = self.__dist_to[v] + 1
                self.__marked[w] = True
                queue.append(w)

    def __validate_vertex(self, v):
        V = len(self.__marked)
        if v < 0 or v >= V:
            raise ValueError("vertex %s is not between 0 and %s" % (
                v, self.__number_of_vertices - 1))

    def has_path_to(self, v):
        self.__validate_vertex(v)
        return self.__marked[v]

    def dist_to(self, v):
        self.__validate_vertex(v)
        return self.__dist_to[v]

    def path_to(self, v):
        self.__validate_vertex(v)
        if not self.has_path_to(v):
            return None

        path = []
        x = v
        while self.__dist_to[x] != 0:
            path.insert(0, x)
            x = self.__edge_to[x]

        path.insert(0, x)
        return path


def main():
    import sys
    from graph import Graph

    txt_file = sys.argv[1]
    G = Graph.from_txt(txt_file)

    s = int(sys.argv[2])
    bfs = BreadthFirstPaths(G, s)

    for v in range(G.V()):
        if bfs.has_path_to(v):
            print("%s to %s (%s): " % (s, v, bfs.dist_to(v))),
            print('-'.join([str(x) for x in bfs.path_to(v)]))
        else:
            print("%d to %d (-):  not connected" % (s, v))


if __name__ == '__main__':
    main()
