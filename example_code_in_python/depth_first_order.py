"""
    depth_first_order.py
    ~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2017 by C. W.
    :license: GPLv3

    Compute preorder and postorder for a digraph
    Runs in O(E + V) time.

    % python depth_first_order.py tinyDAG.txt
       v  pre post
    --------------
       0    0    8
       1    3    2
       2    9   10
       3   10    9
       4    2    0
       5    1    1
       6    4    7
       7   11   11
       8   12   12
       9    5    6
      10    8    5
      11    6    4
      12    7    3
    Preorder:  0 5 4 1 6 9 11 12 10 2 3 7 8
    Postorder: 4 5 1 12 11 10 9 6 0 3 2 7 8
    Reverse postorder: 8 7 2 3 0 6 9 10 11 12 1 5 4

"""
from stack import Stack
from pyqueue import Queue


class DepthFirstOrder(object):

    def __init__(self, G):
        self.__marked = [False] * G.V()
        self.__pre = [-1] * G.V()
        self.__post = [-1] * G.V()

        self.__pre_counter = 0
        self.__post_counter = 0

        self.__pre_order = Queue()
        self.__post_order = Queue()

        for v in range(G.V()):
            if self.__marked[v] is False:
                self.__dfs(G, v)

    def __dfs(self, G, v):
        self.__marked[v] = True
        self.__pre[v] = self.__pre_counter
        self.__pre_counter += 1
        self.__pre_order.enqueue(v)

        for w in G.adj(v):
            if self.__marked[w] is False:
                self.__dfs(G, w)

        self.__post_order.enqueue(v)
        self.__post[v] = self.__post_counter
        self.__post_counter += 1

    def pre(self, v):
        self.__validate_vertex(v)
        return self.__pre[v]

    def post(self, v):
        self.__validate_vertex(v)
        return self.__post[v]

    def pre_order(self):
        return self.__pre_order

    def post_order(self):
        return self.__post_order

    def reverse_post(self):
        reverse = Stack()

        for v in self.__post_order:
            reverse.push(v)

        return reverse

    def __validate_vertex(self, v):
        V = len(self.__marked)
        if v < 0 or v > V:
            raise ValueError("vertex %s is not between 0 and %s" % (
                v, V))


def main():
    import sys
    from digraph import Digraph

    txt_file = sys.argv[1]
    G = Digraph.from_txt(txt_file)

    dfo = DepthFirstOrder(G)
    print("   v  pre post")
    print("--------------")

    for v in range(G.V()):
        print("%4d %4d %4d" % (
            v, dfo.pre(v), dfo.post(v)))

    message = "Preorder:  "
    message += ' '.join([str(v) for v in dfo.pre_order()])
    print(message)

    message = "Postorder: "
    message += ' '.join([str(v) for v in dfo.post_order()])
    print(message)

    message = "Reverse postorder: "
    message += ' '.join([str(v) for v in dfo.reverse_post()])
    print(message)


if __name__ == '__main__':
    main()
