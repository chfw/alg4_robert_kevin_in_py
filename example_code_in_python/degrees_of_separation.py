"""
    degrees_of_separation
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2017 by C. W.
    :license: GPLv3

    % python degrees_of_separation.py routes.txt " " "JFK" # interactive
    LAS
       JFK
       ORD
       PHX
       LAS
    DFW
       JFK
       ORD
       DFW
    EWR
       Not in database.


    Please note the original outpout in DegreesOfSeparation.java for LAS
    was wrong. The output here matches in the one in the text book page 555.

"""
import sys
from symbol_graph import SymbolGraph
from breadth_first_paths import BreadthFirstPaths


def main():
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    source = sys.argv[3]

    sg = SymbolGraph(filename, delimiter)
    g = sg.G()
    if sg.contains(source) is False:
        print(source + " not in database")
        return
    s = sg.index_of(source)
    bfp = BreadthFirstPaths(g, s)

    line = user_input().strip()
    while line != '':
        if sg.contains(line):
            t = sg.index_of(line)
            if bfp.has_path_to(t):
                for v in bfp.path_to(t):
                    print("   " + sg.name_of(v))
            else:
                print("Not connected")
        else:
            print("   Not in database.")

        line = user_input().strip()


def user_input():
    try:
        return raw_input()  # flake8: noqa
    except:
        return input()


if __name__ == '__main__':
    main()
