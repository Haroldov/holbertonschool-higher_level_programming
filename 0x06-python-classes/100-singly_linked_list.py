#!/usr/bin/python3
"""Singly linked list """


class Node:
    """Node Class"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        if next_node is None or type(next_node) is Node:
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """SinglyLinkedList class"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if (self.__head is None):
            self.__head = Node(value)
        elif value <= self.__head.data:
            node = Node(value, self.__head)
            self.__head = node
        else:
            node = self.__head
            while (node.next_node is not None):
                if (node.next_node.data > value):
                    node.next_node = Node(value, node.next_node)
                    break
                else:
                    node = node.next_node
            if (node.next_node is None):
                node.next_node = Node(value)

    def __str__(self):
        node = self.__head
        string = ""
        while (node is not None):
            string += str(node.data) + '\n'
            node = node.next_node
        return string[:-1]
