#!/usr/bin/python3
""" testing for BaseModel class"""
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import unittest
import datetime
from uuid import UUID
import os


class test_FileStorage(unittest.TestCase):
    """ unittest for FileStorage class"""
    def test_file_path(self):
        """ unittest for file path attribute"""
        self.assertEqual(str, type(FileStorage.__file_path))

    def test_objects(self):
        """ unittest for objects attribute"""
        self.assertEqual(dict, type(FileStorage.__objects))

    def test_all(self):
        """ unittest for all method"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """ unittest for new method"""
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_save(self):
        """ unittest for save method"""
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ unittest for reload method """
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            load = obj
        self.assertEqual(BaseModel.to_dict()['name'], load.to_dict()['name'])


if __name__ == "__main__":
    unittest.main()
