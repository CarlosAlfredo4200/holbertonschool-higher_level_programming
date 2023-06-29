#!/usr/bin/python3
"""class """
import json


class Base:
    """
    This is the base class that manages the id attribute
    for all other classes in the project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ List to JSON string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        import json
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs])

        with open(filename, 'w') as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = None
        dummy_instance.update(**dictionary)
        return dummy_instance

    # def update(self, *args, **kwargs):
    #     """
    #     Updates the attributes of the instance.
    #     """
    #     if args:
    #         attr_names = ['id', 'width', 'height', 'size', 'x', 'y']
    #         for attr, value in zip(attr_names, args):
    #             setattr(self, attr, value)

    #     if kwargs:
    #         for attr, value in kwargs.items():
    #             setattr(self, attr, value)

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances loaded from a file.
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**dictionary)
                             for dictionary in dictionaries]
                return instances
        except FileNotFoundError:
            return []
