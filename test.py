import pytest
from functions import add, sub, multiply, divide
# test for a function add, sub, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(2, -3) == -1
    assert add(-2, -3) == -5

def test_sub():
    assert sub(2, 3) == -1
    assert sub(2, -3) == 5
    assert sub(-2, -3) == 1

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(2, -3) == -6
    assert multiply(-2, -3) == 6

def test_divide():
    assert divide(6, 3) == 2
    assert divide(6, -3) == -2
    assert divide(-6, -3) == 2
    assert divide(6, 0) == "Can't divide by zero"



