
from math_series.mathseries_script import fibonacci, lucas

def test_fibonacci_zero():
  actual = fibonacci(0)
  expected = 1
  assert actual == expected

def test_fibonacci_three():
  actual = fibonacci(3)
  expected = 3
  assert actual == expected  

def test_fibonacci_five():
  actual = fibonacci(5)
  expected = 8
  assert actual == expected  

def test_lucas_zero():
  actual = lucas(0)
  expected = 2
  assert actual == expected

def test_lucas_two():
  actual = lucas(2)
  expected = 3
  assert actual == expected

def test_lucas_three():
  actual = lucas(3)
  expected = 4
  assert actual == expected

def test_lucas_four():
  actual = lucas(4)
  expected = 7
  assert actual == expected

def test_sum_series_zero():
  actual = sum_series(0)
  expected = 1
  assert actual == expected



