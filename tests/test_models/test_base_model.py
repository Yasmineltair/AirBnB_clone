#!/usr/bin/python3
""" testing for BaseModel class"""
import json
from sre_constants import SRE_FLAG_IGNORECASE
from models.base_model import BaseModel
import unittest
import datetime
from datetime import datetime as dt
from uuid import UUID
import os


class test_basemodel(unittest.TestCase):
    """ unittest for basemodel class"""
    def test_str(self):
        """ test for str class"""
        BM = BaseModel()
        self.assertEqual(BM.__str__(), "[{}] ({}) {}".format(BM.__class__.__name__, BM.id, BM.__dict__))

    def test_id_uuid(self):
        """ unittest for id"""
        BM1 = BaseModel()
        BM2 = BaseModel()
        BM3 = BaseModel()
        self.assertTrue((BM1.id != BM2.id) and (BM1.id != BM3.id))
        self.assertTrue((BM2.id != BM1.id) and (BM2.id != BM3.id))
        self.assertTrue((BM3.id != BM1.id) and (BM3.id != BM2.id))

    def test_id_type(self):
        """ unittest for id"""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        """ unittest for created at"""
        self.assertEqual(type(BaseModel().created_at), dt)

    def test_updated_at(self):
        """ unittest for updated at"""
        self.assertEqual(type(BaseModel().updated_at), dt)

    def test_save(self):
        """ unittest for save method"""
        BM = BaseModel()
        firstTime = BM.updated_at
        BM.save()
        secondTime = BM.updated_at
        self.assertLess(firstTime, secondTime)

    def test_to_dict(self):
        """ unittest for to_dict method"""
        BM = BaseModel()
        dic = BaseModel().to_dict()
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(type(dic["updated_at"]), str)
        self.assertEqual(type(BM.created_at), dt)
