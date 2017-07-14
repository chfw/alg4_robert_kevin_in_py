"""
    stack.py
    ~~~~~~~~~~~~~~

    :copyright: (c) 2017 by C. W.
    :license: GPLv3

    A generic stack, implemented using a singly-linked list.

    % python stack.py < tobe.txt
    to be not that or be (2 left on stack)
"""
from node import Node


class Stack(object):

    def __init__(self):
        self.__first = None
        self.__n = 0

    def is_empty(self):
        return self.__first is None

    def size(self):
        return self.__n

    def push(self, item):
        new_node = Node(item, self.__first)
        self.__first = new_node
        self.__n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack underflow")

        item = self.__first.item
        self.__first = self.__first.next
        self.__n -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack underflow")

        return self.__first.item

    def __str__(self):
        return ' '.join(list(self))

    def __iter__(self):
        iterator = self.__first

        while iterator:
            yield iterator.item
            iterator = iterator.next


def main():
    import sys
    stack = Stack()

    result = []
    for line in sys.stdin:
        for item in line.strip().split():
            if item != '-':
                stack.push(item)
            elif stack.is_empty() is False:
                result.append(stack.pop())

    print(' '.join(result) + ' (%s left on stack)' % stack.size())


if __name__ == '__main__':
    main()
