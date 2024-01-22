# test_fact.py

from factorialtestlab import *

def test_fact_with_zero():
    assert fact(0) == 1

def test_fact_with_positive_number():
    assert fact(5) == 120
    assert fact(3) == 6

def test_fact_with_negative_number():
    # Assuming the function doesn't handle negative numbers
    # Adjust the test accordingly based on the expected behavior
    with pytest.raises(ValueError):
        fact(-2)

# Add more test cases as needed
