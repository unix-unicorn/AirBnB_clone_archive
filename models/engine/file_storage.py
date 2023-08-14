import json
import os
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        dict_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(dict_obj, file)

    def reload(self):
        """"deserializes the JSON file to __objects ; \
            otherwise, do nothing"""
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place

        new_list = {
                    "User": User, "BaseModel": BaseModel, "City": City,
                    "State": State, "Amenity": Amenity, "Review": Review,
                    "Place": Place
                }
        try:
            with open(self.__file_path, "r", encoding='utf-8') as f:
                dic = json.load(f)
                for value in dic.values():
                    self.new(new_list[value['__class__']](**value))
        except FileNotFoundError:
            pass
