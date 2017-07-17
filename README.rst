Un-official example codes in Python for Algorithms, 4th Edition
================================================================================

.. image:: https://travis-ci.org/chfw/alg4_robert_kevin_in_py.svg?branch=master
   :target: http://travis-ci.org/chfw/alg4_robert_kevin_in_py


It is made for the readers with Python background, who read the following
book::

    Algorithms, 4th Edition
    Copyright (c) 2000 - 2016 Robert Sedgewick and Kevin Wayne

It is also made for me as a reference and hopefully for you too.

Note on the source codes
--------------------------------------------------------------------------------

In order to serve the education purpose, I have ignored the differences of python
2 and python 3 in the following areas:

#. `range` is used instead of `xrange` in python 2, though it is not efficient
   for large inputs

Chapter 1 Fundamentals
--------------------------------------------------------------------------------

================ ============================ ===============================
REF              PROGRAM                      DESCRIPTION
`Chapter 1.3`_   `stack.py`_                  LIFO stack
`Chapter 1.3`_   `pyqueue.py`_ [#f1]_         FIFO stack
`Chapter 1.3`_   `bag.py`_                    multiset
================ ============================ ===============================

.. _bag.py: example_code_in_python/bag.py
.. _pyqueue.py: example_code_in_python/pyqueue.py
.. _stack.py: example_code_in_python/stack.py
.. _Chapter 1.3: http://algs4.cs.princeton.edu/13stacks/index.php
.. [#f1] queue.py conflicts with the built-in library `queue` in python 3. Hence
		 it was renamed to pyqueue.py.

Chapter 4 Graphs
--------------------------------------------------------------------------------

===================== =================================== ===============================
REF                   PROGRAM                             DESCRIPTION
`Chapter 4.1`_        `graph.py`_                         undirected graph
`Chapter 4.1`_        `depth_first_search.py`_            depth-first searcin in a graph
4.1                   `depth_first_paths.py`_             paths in a graph (DFS)
4.2                   `breadth_first_paths.py`_           paths in a graph (BFS)
4.3                   `cc.py`_                            connected components of a graph
`Chapter 4.1`_        `symbol_graph.py`_                  symbol graph
`Chapter 4.1`_        `degrees_of_separation.py`_         degrees of separation     
`Chapter 4.1`_        `digraph.py`_                       directed graph
`Chapter 4.1`_        `directed_dfs.py`_                  directed dfs
`Chapter 4.1`_        `depth_first_directed_graph.py`_    paths in a digraph(DFS)
`Chapter 4.1`_        `breadth_first_directed_graph.py`_  paths in a digraph(BFS)
`Chapter 4.1`_        `directed_cycle.py`_                cycle in a digraph
`Chapter 4.2`_        `depth_first_order.py`_             depth-first order in a digraph
===================== =================================== ===============================

.. _Chapter 4.1: http://algs4.cs.princeton.edu/41graph/index.php
.. _Chapter 4.2: http://algs4.cs.princeton.edu/42digraph/index.php
.. _graph.py: example_code_in_python/graph.py
.. _depth_first_search.py: example_code_in_python/depth_first_search.py
.. _depth_first_paths.py: example_code_in_python/depthth_first_paths.py
.. _breadth_first_paths.py: example_code_in_python/breadth_first_paths.py
.. _cc.py: example_code_in_python/cc.py
.. _symbol_graph.py: example_code_in_python/symbol_graph.py
.. _degrees_of_separation.py: example_code_in_python/degrees_of_separation.py
.. _digraph.py: example_code_in_python/digraph.py
.. _directed_dfs.py: example_code_in_python/directed_dfs.py
.. _depth_first_directed_graph.py: example_code_in_python/depth_first_directed_graph.py
.. _breadth_first_directed_graph.py: example_code_in_python/breadth_first_directed_graph.py
.. _directed_cycle.py: example_code_in_python/directed_cycle.py
.. _depth_first_order.py: example_code_in_python/depth_first_order.py

License
--------------------------------------------------------------------------------

These code is released under GPLv3.
