#!/usr/bin/python3
""" doc """


class Student:
    """ doc """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        keys = self.__dict__.keys()
        values = self.__dict__.values()
        if type(attrs) == list:
            return dict(filter(lambda x: x[0] in attrs, zip(keys, values)))
        else:
            return self.__dict__
