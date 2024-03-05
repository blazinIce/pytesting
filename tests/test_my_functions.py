#here are function based test to  test very simple functions

<<<<<<< HEAD
=======
import time
>>>>>>> ab6427a (first commit)
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
<<<<<<< HEAD
    assert results == 'I love burgers.'
=======
    assert results == 'I love burgers.'


@pytest.mark.slow # this a marker that shows how this test is going to run(slowly)
def test_very_slow():
    time.sleep(5)
    result = my_functions.add(2, 3)
    assert result == 5


@pytest.mark.skip(reason='This test is broken') # this marker skips a test that we dont want to run
def test_add():
    result = my_functions.add(2, 3)
    assert result == 5


@pytest.mark.xfail(reason="we can't devide by zero") # this marker show a test that we know will fail
def test_divide_by_zero_broken():
    my_functions.divide(10,0)
    assert True
>>>>>>> ab6427a (first commit)
