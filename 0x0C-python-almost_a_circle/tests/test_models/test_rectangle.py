"""
Unit test for the Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_instantiation(self):
        """
        Rectangle initializate
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

    def test_raises_errors(self):
        """
        Error testing
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("nombre", 2, 3, 4, 5)
            Rectangle([1], 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "apellido", 3, 4, 5)
            Rectangle(1, (2), 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "ciudad", 4, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "edad", 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-8, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -8, 4, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -9, 5)

    def test_area(self):
        """
        Testing the area of a rectangle
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)
        r2 = Rectangle(100, 40)
        self.assertEqual(r2.area(), 4000)
