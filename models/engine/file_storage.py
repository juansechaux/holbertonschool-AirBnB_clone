#!/usr/bin/python3
'''This is the module for BaseModel Class'''
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
    '''class FileStorage'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file, default=str)

    def reload(self):
        from models.base_model import BaseModel
        """Deserializes the JSON file to __objects."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    list_obj_id = key.split(".")
                    obj_type = eval(list_obj_id[0])()
                    FileStorage.__objects[key] = obj_type
                    '''if obj_type == "User":
                        obj = User(**value)
                        FileStorage.__objects[key] = obj
                    elif obj_type == "BaseModel":
                        obj = BaseModel(**value)
                        FileStorage.__objects[key] = obj
                    elif obj_type == "State":
                        obj = State(**value)
                        FileStorage.__objects[key] = obj
                    elif obj_type == "City":
                        obj = City(**value)
                        FileStorage.__objects[key] = obj
                    elif obj_type == "Amenity":
                        obj = Amenity(**value)
                        FileStorage.__objects[key] = obj
                    elif obj_type == "Place":
                        obj = Place(**value)
                        FileStorage.__objects[key] = obj
                    elif obj_type == "Review":
                        obj = Review(**value)
                        FileStorage.__objects[key] = obj'''
