#!/usr/bin/python 3

"""
Unit test for the Base class
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_instantiation(self):
        """
        Test instantiation increment
        """
        b1 = Base()
        print(b1.id)
        self.assertEqual(b1.id, 1)

        b2 = Base()
        print(b2.id)
        self.assertEqual(b2.id, 2)
