import pytest
from pytest_files.my_functions import *

def test_add():
    result = add(1,1)
    assert result == 2
    assert add(5,5) == 10
    assert add(10, 15) == 25

def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(10/0)

@pytest.mark.parametrize("length, width, expected", [(2,4,8),(4,4,16),(5,5,25)])
def test_multiple_areas(length, width, expected):
    assert Area(length, width).area() == expected

