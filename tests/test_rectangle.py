# here we will test our rectangle class making use of pytest fixtures


def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20  # use the fixture to avoid repeating the function parametres


def test_perimetre(my_rectangle):
    assert my_rectangle.perimeter() == (10 + 20) * 2


def test_not_equal(my_rectangle, another_rectangle):
    assert my_rectangle != another_rectangle  # we check if the 2 rectangles have the same parameters
