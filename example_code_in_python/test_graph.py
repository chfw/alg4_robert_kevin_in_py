import sys
from mock import patch
from nose.tools import eq_
from textwrap import dedent
from six import StringIO


def test_graph():
    import graph
    module_doc = graph.__doc__
    params = _parse_fixtures(module_doc)
    assert len(params) > 0
    for command, result in params:
        args = command.split()[2:]
        with patch.object(sys, 'argv', args):
            with patch('sys.stdout', new_callable=StringIO) as out:
                graph.main()
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
