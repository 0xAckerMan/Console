#!/usr/bin/python3
'''
A command-line interpreter
Uses the cmd module
'''
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
import cmd
import inspect
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models import storage
from models.state import State
from models.user import User
import re
import sys


class HBNBCommand(cmd.Cmd):
    ''' implements 
    quit and EOF to exit
    help
    hbnb - custom prompt
    Empty line for execution
    '''

    intro = '''
**************************************************************    
 _____ _   _ _____    ____ ___  _   _ ____   ___  _     _____ 
|_   _| | | | ____|  / ___/ _ \| \ | / ___| / _ \| |   | ____|
  | | | |_| |  _|   | |  | | | |  \| \___ \| | | | |   |  _|  
  | | |  _  | |___  | |__| |_| | |\  |___) | |_| | |___| |___ 
  |_| |_| |_|_____|  \____\___/|_| \_|____/ \___/|_____|_____|

***************************************************************
    '''
    prompt = '(hbnb)'

    def do_quit(self, line):
        '''Exiting the console'''
        return True
    
    def do_create(self, line):
        """
        Create an instance of BaseModel
        Usage: create <class Name>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif (HBNBCommand.check_class(args[0])):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                my_class = eval(args[0])()
                my_class.save()
                print("{}".format(my_class.id))
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()