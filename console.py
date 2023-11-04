#!/usr/bin/python3
"""Firts Class Base"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class HBNBCommand(cmd.Cmd):
    '''class HBNB that emule a CMD'''
    prompt = "(hbnb) "

    class_list = ["BaseModel", "User"]

    def do_create(self, arg):
        if arg != "":
            if arg not in HBNBCommand.class_list:
                print("** class doesn't exist **")
            else:
                if arg == "BaseModel":
                    arg = BaseModel()
                elif arg == "User":
                    arg = User()
                arg.save()
                print(arg.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Show command to print the string representation of an instance"""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        args = line.split()
        if len(args) == 1:
            if args[0] not in HBNBCommand.class_list:
                print("** class doesn't exist **")
            else:
                new_list = []
                for key in storage.all():
                    if key.startswith(args[0]):
                        value = storage.all()[key]
                        new_list.append(value)
                str_list = [str(obj) for obj in new_list]
                print(str_list)
        else:
            new_list = []
            for key in storage.all():
                value = storage.all()[key]
                new_list.append(value)
            str_list = [str(obj) for obj in new_list]
            print(str_list)

    def do_update(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                with open("file.json", "r") as file:
                    data = FileStorage._FileStorage__objects[key]
                    value = args[3].replace("\"", "")
                    setattr(data, args[2], value)
                    print(value)
                    print(type(value))
                    data.save()
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        print("Exit")
        return True

    def do_EOF(self, arg):
        """Exit the Program"""
        print("Exit")
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
