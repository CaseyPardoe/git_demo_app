import pytest
from factorialtestlab import *


def test_fact_positive():
    assert fact(5) == 120

def test_fact_zero():
    assert fact(0) == 1

def test_fact_negative():
    with pytest.raises(ValueError):
        fact(-1)

def test_fact_non_integer():
    with pytest.raises(TypeError):
        fact(2.5)

def test_fact_large_number():
    assert fact(10) == 3628800


if __name__ == '__main__':
    pytest.main()