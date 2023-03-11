#!/usr/bin/python3
''' File storage class'''
import json
import models

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
        """
        serializes _objects to the JSON file
        """
        with open(FileStorage.__file_path, mode='w', encoding='UTF-8') as f:
            my_obj = {}
            for k, v in FileStorage.__objects.items():
                my_obj[k] = v.to_dict()
            my_str = json.dumps(my_obj)
            f.write(my_str)
    

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
