#!/usr/bin/python3
'''
A command-line interpreter
Uses the cmd module
'''
import cmd


class HBNBCommand(cmd.Cmd):
    ''' implements 
    quit and EOF to exit
    help
    hbnb - custom prompt
    Empty line for execution
    '''

    intro = '''
 _____ _   _ _____    ____ ___  _   _ ____   ___  _     _____ 
|_   _| | | | ____|  / ___/ _ \| \ | / ___| / _ \| |   | ____|
  | | | |_| |  _|   | |  | | | |  \| \___ \| | | | |   |  _|  
  | | |  _  | |___  | |__| |_| | |\  |___) | |_| | |___| |___ 
  |_| |_| |_|_____|  \____\___/|_| \_|____/ \___/|_____|_____|
                                                              

    '''
    prompt = '(hbnb)'

    def do_quit(self, line):
        '''Exiting the console'''
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()