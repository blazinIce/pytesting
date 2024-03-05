#here we perform some class based tests

from source import shapes as shapes
import math

class TestCircle:

    def setup_method(self, method):
        """this function runs a setup code before the test runs"""
        self.circle = shapes.Circle(10)
        print(f"Setting up {method}")

    def teardown_method(self, method):
        """this function runs a tear down code after each test method"""
        print(f"Tearing down {method}")

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        results = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert results == expected

    def test_not_same_area_rectangle(self, my_rectangle):
        """we will test if the area of the rectangle and circle are the same"""
        assert self.circle.area() != my_rectangle.area()