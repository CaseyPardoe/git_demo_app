import pytest
from countlabs import *


def test_count_int():
  assert count([1, 2, 3, 4, 4, 5, 4], 4) == 3
  assert count([1, 2, 4, 0, -2, -4, -4], 0) == 1
  assert count([], 2) == 0

def test_count_str():
    assert count(["apple", "apple", "banana", "pear"], "apple") == 2
    assert count(["pear", "apple", "orange", "banana"], "pear") == 1
    assert count([], "banana") == 0