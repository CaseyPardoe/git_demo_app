import pytest
from vowelslab import * 

def test_vowels_empty_string():
    assert vowels("") == 0

def test_vowels_no_vowels():
    assert vowels("xyz") == 0

def test_vowels_lowercase():
    assert vowels("hello") == 2

def test_vowels_uppercase():
    assert vowels("WORLD") == 1

def test_vowels_mixed_case():
    assert vowels("Python") == 1

def test_vowels_all_vowels():
    assert vowels("aeiou") == 5

def test_vowels_repeated_vowels():
    assert vowels("apple") == 2

def test_vowels_special_characters():
    assert vowels("!@#$%^&*") == 0

def test_vowels_numbers():
    assert vowels("12345") == 0

def test_vowels_mixed_characters():
    assert vowels("a1e2i3o4u5") == 5

if __name__ == "__main__":
    pytest.main()
