"""
    Node for HashTable use
"""
class Node:

    def __init__(self, key, value):
        self.__hash_value = None
        self.__key = key
        self.__value = value
        self.__next = None

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

if __name__ == "__main__":
    n = Node("abc", 99)
    print(n.key, n.value)
    n.key = "def"
    n.value = -1
    print(n.key, n.value)
