#!/usr/bin/python3
"""FileStorage Definition"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ main File Storage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ all, return objects dict """
        return self.__objects

    def new(self, obj):
        """ creates new instance with id """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ saves an instance into JSON file at @__file_path """
        out_dict = {}
        for key, val in self.__objects.items():
            out_dict[key] = val.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(out_dict, f)

    def reload(self):
        """ reloads JSON file at @__file_path into instance"""
        try:
            with open(self.__file_path, "r") as f:
                objects = json.load(f)
                for val in objects.values():
                    class_name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(class_name)(**val))
        except FileNotFoundError:
            return
