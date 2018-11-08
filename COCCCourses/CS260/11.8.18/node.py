"""
    Node for btree use
"""
class Node:

    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right

    @property
    def data(self):
        return self.__data

    '''
    @data.setter
    def data(self, data):
        self.__data = data'''

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, data):
        self.__left = Node(data)

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, data):
        self.__right = Node(data)

    def __str__(self):
        return str(self.data)
