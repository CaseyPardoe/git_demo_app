import pytest
from listofsquareslab import * 

def test_list_of_squares():
    result = list_of_squares(5)
    assert result == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    result = list_of_squares(0)
    assert result == {}

    with pytest.raises(ValueError):
        list_of_squares(-3)

    result = list_of_squares(1000)
    assert result[500] == 500 * 500

    with pytest.raises(TypeError):
        list_of_squares(3.5)

    with pytest.raises(TypeError):
        list_of_squares("abc")

    with pytest.raises(TypeError):
        list_of_squares([1, 2, 3])

    with pytest.raises(TypeError):
        list_of_squares(None)


