# here i demonstrate how to parametrize a test to run test for multiple similar objects(squares)
import source.shapes as shapes
import pytest


@pytest.mark.parametrize("side_length, expected_area",[(2,4),(4,16),(20,400)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(2, 8), (6, 24), (4, 16)])
def tests_multiple_square_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter
