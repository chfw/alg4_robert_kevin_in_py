import sys
from mock import patch
from nose.tools import eq_
from textwrap import dedent
from six import StringIO


def test_bag():
    module = __import__('bag')
    _verify_module(module)


def test_stack():
    module = __import__('stack')
    _verify_module(module)


def test_pyqueue():
    module = __import__('pyqueue')
    _verify_module(module)


def test_graph():
    module = __import__('graph')
    _verify_module(module)


def test_depth_first_search():
    module = __import__('depth_first_search')
    _verify_module(module)


def test_depth_first_paths():
    module = __import__('depth_first_paths')
    _verify_module(module)


def test_breadth_first_search():
    module = __import__('breadth_first_paths')
    _verify_module(module)


def test_cc():
    module = __import__('cc')
    _verify_module(module)


def test_symbol_graph():
    module = __import__('symbol_graph')
    _verify_module(module)


def test_symbol_digraph():
    module = __import__('symbol_digraph')
    _verify_module(module)


def test_degrees_of_separation():
    module = __import__('degrees_of_separation')
    _verify_module(module)


def test_digraph():
    module = __import__('digraph')
    _verify_module(module)


def test_directed_dfs():
    module = __import__('directed_dfs')
    _verify_module(module)


def test_depth_first_directed_paths():
    module = __import__('depth_first_directed_paths')
    _verify_module(module)


def test_breadth_first_directed_paths():
    module = __import__('breadth_first_directed_paths')
    _verify_module(module)


def test_directed_cycle():
    module = __import__('directed_cycle')
    _verify_module(module)


def test_depth_first_order():
    module = __import__('depth_first_order')
    _verify_module(module)


def test_topological():
    module = __import__('topological')
    _verify_module(module)


# bottom


def _verify_module(module):
    params = _parse_fixtures(module.__doc__)
    assert len(params) > 0
    for command, result in params:
        if "# interactive" in command:
            interactive = {}
            current_command = None
            for line in result:
                if line.startswith(' '):
                    interactive[current_command].append(line)
                else:
                    the_input = line
                    if the_input not in interactive:
                        interactive[the_input] = []
                        current_command = the_input

            for user_input, output in interactive.items():
                with patch('%s.user_input' % module.__name__) as the_input:
                    the_input.side_effect = [user_input, '']
                    _verify_simple_commands(command.split('#')[0],
                                            output, module)

        elif "<" in command:
            run_command, stdin_file = command.split('<')
            with open(stdin_file.strip(), 'r') as f:
                with patch('sys.stdin', new=f):
                    _verify_simple_commands(run_command.strip(),
                                            result, module)
        else:
            _verify_simple_commands(command, result, module)


def _verify_simple_commands(command, result, module):
    args = _split_commands(command)[2:]
    custom_module = args[0].split('.')[0]
    if module.__name__ != custom_module:
        # python graph.py appeared in breadth_first_paths
        module = __import__(custom_module)
    with patch.object(sys, 'argv', args):
        with patch('sys.stdout', new_callable=StringIO) as out:
            module.main()
            _verify_results(out.getvalue().split('\n'), result)


def _verify_results(actual, expected):
    if len(actual) > len(expected):
        _line_by_line_compare(actual[:len(expected)], expected)
    else:
        _line_by_line_compare(actual, expected)


def _line_by_line_compare(actual, expected):
    for left, right in zip(actual, expected):
        if len(left) > len(right):
            if right.endswith('...'):
                right = right[:-3]
                assert left.startswith(right)
            else:
                eq_(left, right)
        else:
            eq_(left, right)


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


def _split_commands(command_string):
    if '" "' in command_string:
        command_string = command_string.replace('" "', '"_"')
    results = [_cleanse_command(token) for token in command_string.split()]
    return results


def _cleanse_command(token):
    if token == '"_"':
        return ' '
    elif token.startswith('"'):
        return token[1:-1]
    else:
        return token
