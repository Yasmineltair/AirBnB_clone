#!/usr/bin/python3
""" testing for user class"""
import models
from models.user import User
import unittest
import os


class test_user(unittest.TestCase):
    """ unittest for class user"""
    def test_email(self):
        """ test email"""
        self.assertEqual(str, type(User.email))

    def test_password(self):
        """ test password"""
        self.assertEqual(str, type(User.password))

    def test_first_name(self):
        """ test first_name"""
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        """ test last name"""
        self.assertEqual(str, type(User.last_name))


if __name__ == "__main__":
    unittest.main()
