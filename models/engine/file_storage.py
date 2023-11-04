#!/usr/bin/python3
'''This is the module for BaseModel Class'''
import json
import os


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
                    obj = BaseModel(**value)
                    FileStorage.__objects[key] = obj
