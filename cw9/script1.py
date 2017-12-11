import pytest

def function(n):
    return {
        1:'jeden',
        2:'dwa',
        3:'trzy'
    }.get(n)


def test_should_Return1():
    #given
    number = 'jeden'
    expectedValue = 1
    #when
    result = function(number)
    #then
    assert result == expectedValue


def test_should_Return2():
    #given
    number = 'dwa'
    expectedValue = 2
    #when
    result = function(number)
    #then
    assert result == expectedValue

def test_should_Return3():
    # given
    number = 'trzy'
    expectedValue = 3
    # when
    result = function(number)
    # then
    assert result == expectedValue