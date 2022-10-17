"""Tests for the solution of your exercise."""
"""DO NOT CHANGE THIS FILE!"""

from frequencies import frequencies

def test_mixed_list():
    input = ['0', 4,4,'4','d','d','e',0,'a','d','4']
    output = frequencies(input)
    assert output['4'] == 4
    assert output['d'] == 3
    assert output['e'] == 1
    assert output['a'] == 1
    assert output['0'] == 2
    assert 4 not in output.keys()
    assert 0 not in output.keys()

def test_empty_list():
    input = []
    output = frequencies(input)
    assert output == {}

def test_example_1():
    input = ['a', 'a', 'b', 'b', 'b', 'c']
    output = frequencies(input)
    assert output['a'] == 2
    assert output['b'] == 3
    assert output['c'] == 1

def test_example_2():
    input = [100, 'Hello', '100', '100', 100]
    output = frequencies(input)
    assert output['100'] == 4
    assert output['Hello'] == 1
    assert 100 not in output.keys()
