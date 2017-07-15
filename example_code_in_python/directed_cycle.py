"""
    directed_cyle.py
    ~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2017 by C. W.
    :license: GPLv3

    Finds a directed cycle in a digraph
    Runs in O(E + V) time.

    % python directed_cycle.py tinyDG.txt
    Directed cycle: 3 5 4 3

    % python directed_cycle.py tinyDAG.txt
    No directed cycle

"""
from stack import Stack


class DirectedCycle(object):

    def __init__(self, G):
        self.__marked = [False] * G.V()
        self.__on_stack = [False] * G.V()
        self.__edge_to = [0] * G.V()
        self.__cycle = None
        
        for v in range(G.V()):
            if self.__marked[v] is False and self.__cycle is None:
                self.__dfs(G, v)

    def __dfs(self, G, v):
        self.__on_stack[v] = True
        self.__marked[v] = True

        for w in G.adj(v):
            if self.__cycle is not None:
                break
            elif self.__marked[w] is False:
                self.__edge_to[w] = v
                self.__dfs(G, w)
            elif self.__on_stack[w]:
                self.__cycle = Stack()
                x = v
                while x != w:
                    self.__cycle.push(x)
                    x = self.__edge_to[x]

                self.__cycle.push(w)
                self.__cycle.push(v)
                assert self.__check()

        self.__on_stack[v] = False

    def has_cycle(self):
        return self.__cycle is not None

    def cycle(self):
        return self.__cycle

    def __check(self):
        if self.has_cycle():
            first = last = -1
            for v in self.cycle():
                if first == -1:
                    first = v
                last = v
            if first != last:
                print("cycle begins with %d and ends with %d" % (first, last))
                return False
        return True


def main():
    import sys
    from digraph import Digraph

    txt_file = sys.argv[1]
    G = Digraph.from_txt(txt_file)

    finder = DirectedCycle(G)
    if finder.has_cycle():
        message = "Directed cycle: "
        message += ' '.join([str(v) for v in finder.cycle()])
        print(message)
    else:
        print("No directed cycle")


if __name__ == '__main__':
    main()
