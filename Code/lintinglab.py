"""
Module: lintinglab

This module contains a function to count the occurrences of an item in a sequence.
"""

def count(sequence, item):
    """
    Count the occurrences of 'item' in 'sequence'.

    Args:
        sequence (iterable): The sequence to search.
        item: The item to count.

    Returns:
        int: The number of occurrences of 'item' in 'sequence'.
    """
    count_result = 0

    for n in sequence:
        if n == item:
            count_result += 1

    return count_result
