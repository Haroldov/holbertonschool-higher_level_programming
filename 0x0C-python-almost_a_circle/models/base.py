#!/usr/bin/python3
import json
""" base module """


class Base:
    """ class Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ doc """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ doc """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ doc """
        filename = cls.__name__ + ".json"
        listDic = []
        for instance in list_objs:
            listDic.append(instance.to_dictionary())
        with open(filename, 'w') as f:
            if list_objs is None:
                json.dump([], f)
            else:
                json.dump(listDic, f)

    @staticmethod
    def from_json_string(json_string):
        """ doc """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ doc """
        dummy = cls(1, 1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ doc """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                dics = cls.from_json_string(f.read())
                instances = []
                for dic in dics:
                    instances.append(cls.create(**dic))
                return instances
        except:
            return []
