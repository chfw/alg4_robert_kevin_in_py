"""
    queue.py
    ~~~~~~~~~~~~~~

    :copyright: (c) 2017 by C. W.
    :license: GPLv3

    A generic queue, implemented using a linked list

    % python pyqueue.py < tobe.txt
    to be or not to be (2 left on queue)
"""


class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Queue(object):

    def __init__(self):
        self.__first = None
        self.__last = None
        self.__n = 0

    def is_empty(self):
        return self.__first is None

    def size(self):
        return self.__n

    def peak(self):
        if self.is_empty():
            raise ValueError("Queue underflow")

        return self.__first.item

    def enqueue(self, item):
        old_last = self.__last
        self.__last = Node(item, None)
        if self.is_empty():
            self.__first = self.__last
        else:
            old_last.next = self.__last
        self.__n += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue underflow")

        item = self.__first.item
        self.__first = self.__first.next

        self.__n -= 1
        return item

    def __str__(self):
        return ' '.join(list(self))

    def __iter__(self):
        iterator = self.__first

        while iterator:
            yield iterator.item
            iterator = iterator.next


def main():
    import sys

    queue = Queue()

    result = []
    for line in sys.stdin:
        for item in line.strip().split():
            if item != '-':
                queue.enqueue(item)
            elif queue.is_empty() is False:
                result.append(queue.dequeue())

    print(' '.join(result) + ' (%s left on queue)' % queue.size())


if __name__ == '__main__':
    main()
