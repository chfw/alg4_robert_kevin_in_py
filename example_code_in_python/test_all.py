import sys
from mock import patch
from nose.tools import eq_
from textwrap import dedent
from six import StringIO


MODULES = [
    "graph",
    "depth_first_search",
    "breadth_first_paths"
]


def test_example_codes():
    for module_name in MODULES:
        print("Verifying %s.py ..." % module_name)
        module = __import__(module_name)
        _verify_module(module)
        print("Done")


def _verify_module(module):
    params = _parse_fixtures(module.__doc__)
    assert len(params) > 0
    for command, result in params:
        print(command)
        args = command.split()[2:]
        custom_module = args[0].split('.')[0]
        if module.__name__ != custom_module:
            # python graph.py appeared in breadth_first_paths
            module = __import__(custom_module)
        with patch.object(sys, 'argv', args):
            with patch('sys.stdout', new_callable=StringIO) as out:
                module.main()
                _verify_results(out.getvalue().strip().split('\n'), result)


def _verify_results(actual, expected):
    if len(actual) > len(expected):
        eq_(actual[:len(expected)], expected)
    else:
        eq_(actual, expected)


def _parse_fixtures(docstring):
    lines = dedent(docstring).split('\n')
    record_result = False
    results = []
    params = []
    command = None
    for line in lines:
        if record_result:
            if line == '' or line == '...':
                params.append((command, results))
                results = []
                command = None
                record_result = False
            else:
                results.append(line)
        elif line.startswith('%'):
            command = line
            record_result = True
    return params
