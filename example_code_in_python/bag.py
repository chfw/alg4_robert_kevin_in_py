"""
    bag.py
    ~~~~~~~~~~~~~~

    :copyright: (c) 2017 by C. W.
    :license: GPLv3

    A generic bag or multiset, implemented using a singly-linked
    list.

    % python bag.py < tobe.txt
    size of bag = 14
    is
    -
    -
    -
    that
    -
    -
    be
    -
    to
    not
    or
    be
    to

"""


from collections import namedtuple


class Node(namedtuple("Node", "item next")):
    __slots__ = ()

    def __str__(self):
        return self.item


class Bag(object):
    def __init__(self):
        self.__first = None
        self.__n = 0

    def is_empty(self):
        return self.__first is None

    def size(self):
        return self.__n

    def add(self, item):
        oldfirst = self.__first
        self.__first = Node(item, oldfirst)
        self.__n += 1

    def __iter__(self):
        iterator = self.__first
        while iterator:
            yield iterator
            iterator = iterator.next


def main():
    import sys

    bag = Bag()
    for line in sys.stdin:
        for item in line.strip().split():
            bag.add(item)

    print("size of bag = %s" % bag.size())
    for s in bag:
        print(s)


if __name__ == '__main__':
    main()
