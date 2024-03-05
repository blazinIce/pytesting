#here are function based test to  test very simple functions

import pytest
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(2, 3)
    assert result == 5

def test_divide():
    result = my_functions.divide(10, 2)
    assert result == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10,0)
    assert True

def test_add_text():
    results = my_functions.add('I love ', 'burgers.')
    assert results == 'I love burgers.'