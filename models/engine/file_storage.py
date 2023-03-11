#!/usr/bin/python3
''' File storage class'''
import json
import models
from models.user import User

class FileStorage:
    '''
    Class implementation that serializes instance to json
    and deserializes JSON to instances
    '''
    

    __file_path = 'file.json'
    __objects = {}

    
    def all(self):
        '''returns all objects'''
        return FileStorage.__objects
    
    def new(self, obj):
        '''
        Sets key for object
        args:
            @obj
        '''
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
    
    def save(self):
        with open(self.__file_path, "w", encoding="utf-8") as file:
            dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dict, file)
    

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, mode='r') as f:
                r = json.load(f)
                for k, v in r.items():
                    cls_name = k.split('.')[0]
                    my_obj = eval(cls_name)(**v)
                    self.new(my_obj)
        except:
            pass
