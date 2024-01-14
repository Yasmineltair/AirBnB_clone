#!/usr/bin/python3
""" testing for city class"""
from console import HBNBCommand
import unittest
import os


class test_HBNBCommand(unittest.TestCase):
    """ unittest for HBNBCommand class"""
    def test_allowed_classes(self):
        """ test HBNBCommand allowed_classes"""
        self.assertEqual(list, type(HBNBCommand.allowed_classes))

    def test_allowed_methods(self):
        """ test HBNBCommand allowed_methods"""
        self.assertEqual(list, type(HBNBCommand.allowed_methods))


if __name__ == "__main__":
    unittest.main()
