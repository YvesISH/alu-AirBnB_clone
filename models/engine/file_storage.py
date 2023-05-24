#!/usr/bin/python3
"""This defines a class to manage file storage"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ 
    This is a storage engine
    """
    __file_path = 'storage.json'

    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """
        Add obj with key <obj class name>
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """
            Serialize '__objects' to the JSON file '__file_path'
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """
            Deserialize JSON file '__file_path' to '__objects' dictionary,
            if file exists else the method does nothing.
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
