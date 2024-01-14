#!/usr/bin/python3
""" testing for amenity class"""
import models
from models.amenity import Amenity
import unittest
import os


class test_amenity(unittest.TestCase):
    """ unittet for amenity """
    def test_name(self):
        """ test name"""
        self.assertEqual(str, type(Amenity.name))


if __name__ == "__main__":
    unittest.main()
