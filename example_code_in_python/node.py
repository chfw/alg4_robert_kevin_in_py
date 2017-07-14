"""
    node.py
    ~~~~~~~~~~~~~~

    :copyright: (c) 2017 by C. W.
    :license: GPLv3
"""
from collections import namedtuple


class Node(namedtuple("Node", "item next")):
    __slots__ = ()

    def __str__(self):
        return self.item
