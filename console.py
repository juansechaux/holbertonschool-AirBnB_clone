#!/usr/bin/python3
"""Firts Class Base"""
import cmd


class HBNBCommand(cmd.Cmd):
    '''class HBNB that emule a CMD'''
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        print("exit")
        return True

    def do_EOF(self, arg):
        """Exit the Program"""
        print("exit")
        return True

    def empyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        print("")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
