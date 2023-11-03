#!/usr/bin/python3
'''This is the module for BaseModel Class'''
import json
import os

print('Segundo paso initialization')
class FileStorage:
    '''class FileStorage'''

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        # self.reload()
        pass

    '''@property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, file_path):
        self.__file_path = file_path

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, objects):
        self.__objects = objects'''

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
        print('Tercero paso initialization')
        """Deserializes the JSON file to __objects."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    print(class_name)
                    #cls = eval(class_name)
                    obj = BaseModel(**value)
                    FileStorage.__objects[key] = obj

