"""
    breadth_first_directed_paths.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2017 by C. W.
    :license: GPLv3

    Run breadth-first search on a digraph.
    Runs in O(E + V) time.

    % python breadth_first_directed_paths.py tinyDG.txt 3
    3 to 0 (2):  3->2->0
    3 to 1 (3):  3->2->0->1
    3 to 2 (1):  3->2
    3 to 3 (0):  3
    3 to 4 (2):  3->5->4
    3 to 5 (1):  3->5
    3 to 6 (-):  not connected
    3 to 7 (-):  not connected
    3 to 8 (-):  not connected
    3 to 9 (-):  not connected
    3 to 10 (-):  not connected
    3 to 11 (-):  not connected
    3 to 12 (-):  not connected
"""
from pyqueue import Queue
from stack import Stack


class BreadthFirstDirectedPaths(object):

    def __init__(self, G, sources):
        self.__marked = [False] * G.V()
        self.__dist_to = [float('inf')] * G.V()
        self.__edge_to = [0] * G.V()

        self.__validate_vertices(sources)
        self.__bfs(G, sources)

    def __bfs(self, G, sources):
        q = Queue()
        for s in sources:
            self.__marked[s] = True
            self.__dist_to[s] = 0
            q.enqueue(s)

        while q.is_empty() is False:
            v = q.dequeue()
            for w in G.adj(v):
                if self.__marked[w] is False:
                    self.__edge_to[w] = v
                    self.__dist_to[w] = self.__dist_to[v] + 1
                    self.__marked[w] = True
                    q.enqueue(w)

    def __validate_vertex(self, v):
        V = len(self.__marked)
        if v < 0 or v >= V:
            raise ValueError("vertex %s is not between 0 and %s" % (
                v, self.__number_of_vertices - 1))

    def __validate_vertices(self, vertices):
        for v in vertices:
            self.__validate_vertex(v)

    def has_path_to(self, v):
        self.__validate_vertex(v)
        return self.__marked[v]

    def dist_to(self, v):
        self.__validate_vertex(v)
        return self.__dist_to[v]

    def path_to(self, v):
        self.__validate_vertex(v)

        if self.has_path_to(v) is False:
            return None

        path = Stack()
        x = v
        while self.__dist_to[x] != 0:
            path.push(x)
            x = self.__edge_to[x]

        path.push(x)
        return path


def main():
    import sys
    from digraph import Digraph

    file_name = sys.argv[1]

    G = Digraph.from_txt(file_name)
    s = int(sys.argv[2])
    bfs = BreadthFirstDirectedPaths(G, [s])

    for v in range(G.V()):
        if bfs.has_path_to(v):
            content = "%s to %s (%d):  " % (s, v, bfs.dist_to(v))
            for x in bfs.path_to(v):
                if x == s:
                    content += str(x)
                else:
                    content += '->' + str(x)
            print(content)
        else:
            print("%d to %d (-):  not connected" % (s, v))


if __name__ == '__main__':
    main()
