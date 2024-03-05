# here we create our test fixtures so the can be available globally

import source.shapes as shapes
import pytest


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)  # declare the parameter you want to fix


@pytest.fixture
def another_rectangle():
    return shapes.Rectangle(20, 10)  # we declare parameters for another rectangle
