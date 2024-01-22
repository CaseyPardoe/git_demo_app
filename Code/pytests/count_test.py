from test_labs.countlab import *
import pytest

def test_count_empty_sequence():
    # Test case for an empty sequence
    sequence = []
    item = 42
    result = count(sequence, item)
    assert result == 0, f"Expected count of {item} is 0 for an empty sequence, but got {result}"

def test_count_item_not_in_sequence():
    # Test case for when the item is not present in the sequence
    sequence = [1, 2, 3, 4, 5]
    item = 6
    result = count(sequence, item)
    assert result == 0, f"Expected count of {item} is 0 when item is not in the sequence, but got {result}"

def test_count_mixed_types():
    # Test case for a sequence with mixed types
    sequence = [1, 'apple', 2, 'orange', 'apple', 'banana', 1, 'apple']
    item = 'apple'
    result = count(sequence, item)
    assert result == 3, f"Expected count of '{item}' is 3 in a sequence with mixed types, but got {result}"

# Run all the tests
test_count_integers()
test_count_strings()
test_count_empty_sequence()
test_count_item_not_in_sequence()
test_count_mixed_types()