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

In order to serve the education purpose, I have hidden the differences of python
2 and python 3 in the following areas:

#. `range` is used instead of `xrange` in python 2, though it is not efficient
   for large inputs

Chapter 1 Fundamentals
--------------------------------------------------------------------------------

===== ============================ ===============================
REF   PROGRAM                      DESCRIPTION
.     `bag.py`_                    multiset
===== ============================ ===============================

.. _bag.py: example_code_in_python/bag.py



Chapter 4 Graphs
--------------------------------------------------------------------------------

===================== ============================ ===============================
REF                   PROGRAM                      DESCRIPTION
.                     `graph.py`_                  undirected graph
.                     `depth_first_search.py`_     depth-first searcin in a graph
4.1                   `depth_first_paths.py`_      paths in a graph (DFS)
4.2                   `breadth_first_paths.py`_    paths in a graph (BFS)
4.3                   `cc.py`_                     connected components of a graph
.                     `symbol_graph.py`_           symbol graph
`-<ch41>`_            `degrees_of_separation`_     degrees of separation     
===================== ============================ ===============================

.. _ch41: http://algs4.cs.princeton.edu/41graph/index.php
.. _graph.py: example_code_in_python/graph.py
.. _depth_first_search.py: example_code_in_python/depth_first_search.py
.. _depth_first_paths.py: example_code_in_python/depthth_first_paths.py
.. _breadth_first_paths.py: example_code_in_python/breadth_first_paths.py
.. _cc.py: example_code_in_python/cc.py
.. _symbol_graph.py: example_code_in_python/symbol_graph.py
.. _degrees_of_separation.py: example_code_in_python/degrees_of_separation.py

License
--------------------------------------------------------------------------------

These code is released under GPLv3.
