#!/usr/bin/python3
"""
this is the launch point of our CLI
which imports and customize the cmd.Cmd class
"""

import cmd
from console_util import cmd_utils
from models import storage, storage_type, db
from models.engine import valid_models
from os import system


# chepe-work:
# make do_create with params NOT create invalid attributes
class HBNBCommand(cmd.Cmd):
    """ our reimplementation of cmd.Cmd
    """
    prompt = '(hbnb) '

    def do_storage(self, args):
        '''
        output which backend storage system is being used and which database
        if any
        '''
        print("working in {} storage mode".format(storage_type))
        if storage_type == 'db':
            print("using database {}".format(db))

    def do_models(self, args):
        '''
        list the given or all available models and their properties
        '''
        if not args:
            for name, model in valid_models().items():
                print(name, end="\n| ")
                cmd_utils.print_fields(model)
                print(end="\n\n")
        else:
            model = self.get_class(args)
            cmd_utils.print_fields(model)
            print()

    do_model = do_models

    def do_create(self, arg):
        'creates a new instance of BaseModel'
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        else:
            model_class = valid_models().get(args[0])
            if model_class is None:
                print("** class doesn't exist **")
                return
            else:
                try:
                    key_value_dict = cmd_utils.process_key_value_pairs(
                        args[1:])
                except ValueError:
                    print("malformed arguments. no record created")
                    return

                unnullables = cmd_utils.unnullables(model_class)
                for unnullable in unnullables:
                    if unnullable not in key_value_dict.keys():
                        print("a non-nullable parameter has not \
                              been specified."
                              " no record created\n"
                              "non-nullable fields: ",
                              unnullables)
                        return

                for key in key_value_dict.keys():
                    if key not in cmd_utils.get_fields(model_class):
                        print("invalid field name(s) passed. no model created")
                        return

                new_obj = model_class(**key_value_dict)
                new_obj.save()
                print(new_obj.id)

    def do_show(self, args):
        'outputs representation of an instance given the class name and id'
        instance = self.get_instance(args)
        if instance is None:
            return
        else:
            print(str(instance))

    def do_get(self, usr_input):
        '''
        directly accesses object from storage
        '''
        if usr_input:
            usr_input = usr_input.split()
            id_num = usr_input[1] if len(usr_input) > 1 else None
            model = usr_input[0] if len(usr_input) > 0 else None
            model = valid_models().get(model)
        else:
            id_num = None
            model = None
        if model:
            print("object extracted from storage:")
            print(storage.get(model, id_num))
        else:
            print("** no valid class specified **")

    def do_count(self, usr_input):
        '''
        counts all of the objects of a given class in storage
        if no class is given then it counts everything in storage instead
        '''
        if usr_input:
            model = self.get_class(usr_input)
            if not model:
                print("** invalid class specified **")
                return
            print("total {} objects in storage:".format(usr_input))
        else:
            model = None
            print("total objects in storage:")
        print(storage.count(model))

    def do_all(self, args):
        """ outputs string representations for every existing
        instance or for all of a class
        """
        obj_list = []

        if not args:
            for value in storage.all().values():
                obj_list.append(str(value))
        else:
            class_given = args.split()
            class_given = class_given[0]
            model_class = valid_models().get(class_given)
            if model_class is not None:
                for key, value in storage.all().items():
                    if key.startswith(class_given):
                        obj_list.append(str(value))
            else:
                print("** class doesn't exist **")
                return

        print(obj_list)
        # for obj in obj_list:
        #    print(obj)
        #    print("----------------")

    do_list = do_all

    def do_update(self, arg):
        """ updates the instance given by class_name and id.
        usage: update <class> <id> <attr> "<val>"
        """

        instance = self.get_instance(arg)
        if instance is None:
            return

        attr_val = cmd_utils.parse_attributes(arg)
        if attr_val is None:
            return

        attr = attr_val[0]
        value = attr_val[1]

        cmd_utils.update(instance, attr, value)

    def do_destroy(self, arg):
        'delete instance given by the class name and id'
        if arg.lower() == 'all':
            # define expunge() for DBStorage and FileStorage
            # and call storage.expunge()
            return
        instance = self.get_instance(arg)
        if instance is None:
            return
        else:
            instance.delete()
            storage.save()

    do_delete = do_destroy

    def do_clear(self, args):
        '''
        wipes the terminal window
        '''
        system('clear')

    def do_quit(self, arg):
        'exit this CLI instance hbnb'
        return True

    def do_exit(self, arg):
        'exit this CLI instance hbnb'
        raise SystemExit

    def do_EOF(self, arg):
        '''exit this CLI instance hbnb'''
        raise SystemExit

    def emptyline(self):
        pass

    def get_instance(self, args):
        args = args.split()
        class_name = args[0] if len(args) > 0 else None
        id_num = args[1] if len(args) > 1 else None
        model_class = valid_models().get(class_name)

        if class_name is None:
            print('** class name missing **')
            return None
        elif model_class is None:
            print("** class doesn't exist **")
            return None
        elif id_num is None:
            print('** instance id missing **')
            return None
        else:
            key = class_name + "." + id_num
            instance = storage.all().get(key)
            if instance is None:
                print('** no instance found **')
                return None
            return instance

    def get_class(self, args):
        '''
        return class from string
        '''
        model = args.split()
        model = model[0]
        model = valid_models().get(model)
        return model


if __name__ == '__main__':
    HBNBCommand().cmdloop()
