# imports
from math_series.math_series import fibonacci, lucas, sum_series

# fibonacci tests
def test_math_series_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

# lucas tests
def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected

# sum_series tests
def test_sum_fib():
    actual = sum_series(0)
    expected = fibonacci(0)
    assert actual == expected
    
def test_sum_luc():
    actual = sum_series(1)
    expected = lucas(1)
    assert actual == expected