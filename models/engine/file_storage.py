#!/usr/bin/python3
""" 
contain class FileStorage that serializes instances to a JSON
file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file to instances:"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  returns the dictionary __objects """
        return FileStorage.__objects
    
    def new(self, obj):
