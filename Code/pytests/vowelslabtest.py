import pytest
from vowelslab import * 

def test_vowels():
    assert vowels("xyz") == 0
    assert vowels("aeiou") == 5
    assert vowels("AEIOU") == 5
    assert vowels("Hello World") == 3

def test_vowels_numbers():
    assert vowels("12345") == 0

def test_vowels_mixed_characters():
    assert vowels("a1e2i3o4u5") == 5

if __name__ == "__main__":
    pytest.main()
