#!/usr/bin/python3
"""
this is the launch point of our CLI
which imports and customize the cmd.Cmd class
"""

class CmdUtils():
    """
    """

    def unnullables(self, model):
        unnullables = []
        for k, v in model.__table__.columns.items():
            if (v.nullable is False and
                k not in ['id', 'created_at', 'updated_at']):
                unnullables.append(k)
        return unnullables

    def print_fields(self, model):
        fields = self.get_fields(model)
        for field in fields:
            if field not in ['id', 'created_at', 'updated_at']:
                print(field, end=" | ")

    def get_fields(self, model):
        fields = []
        for attr in model.__dict__.keys():
            if attr[0] != '_':
                fields.append(attr)
        return fields

    def string_to_number(self, num_string):
        if num_string.count(".") == 1:
            try:
                number = float(num_string)
            except ValueError:
                return None
        else:
            try:
                number = int(num_string)
            except ValueError:
                return None
        return number

    def clean_string(self, old_string):
        new_string = old_string.replace("_", " ")
        new_string = new_string[1:-1]
        new_string = new_string.replace('"', '\\"')
        return new_string

    def update(self, instance, attr, value):
        if hasattr(instance, attr):
            attr_type = type(getattr(instance, attr))
            try:
                value = attr_type(value)
                setattr(instance, attr, value)
                instance.save()
            except (ValueError, TypeError):
                print("** value given could not be typecast correctly **")
        else:
            print("** no such attribute found **")

    def process_key_value_pairs(self, key_value_list):
        """
        parse arguments passed and set values accordingly
        syntax: create ClassName keyA="valueA" keyB="valueB" ...
        """
        key_value_dict = {}
        for key_value in key_value_list:
            #try:
            (key, value) = key_value.split("=")
            if (value.startswith('"')
                and value.endswith('"')):
                value = self.clean_string(value)
            elif (number := self.string_to_number(value)) is not None:
                value = number
            else:
                continue
            key_value_dict.update({key: value})
        return key_value_dict

    def parse_attributes(self, args):
        attr = args.split()
        attr = attr[2] if len(attr) > 2 else None
        if args.find('"') > 0:
            value = args.split('"')
            value = value[1] if len(value) > 1 else None
        elif args.find("'") > 0:
            value = args.split("'")
            value = value[1] if len(value) > 1 else None
        else:
            value = args.split()
            value = value[3] if len(value) > 3 else None

        if attr is None:
            print('** attribute name missing **')
            return None
        elif value is None:
            print('** value missing **')
            return None
        else:
            return (attr, value)

cmd_utils = CmdUtils()
