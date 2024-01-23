import pytest
from listofsquareslab import * 

def test_list_of_squares():
    assert list_of_squares(1) == {1: 1}
    assert list_of_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    assert list_of_squares(10) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}