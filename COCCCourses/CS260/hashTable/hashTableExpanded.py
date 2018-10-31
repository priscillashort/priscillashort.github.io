"""
   HashTable example expanded
"""

from node import Node
 
class HashTable():
 
    def __init__(self, size = 100, load_factor=.75):
        self.store_size = size
        self.store = [None] * self.store_size
        self.count = 0
 
 
    def size(self):
        return self.count
 
    def __str__(self):
        return str([(item.key, item.value) for idx, item in enumerate(self.store) if item is not None])
 
    def __getitem__(self, key):
        hash_val = self.hash(key)

        while (self.store[hash_val] is not None and
                self.store[hash_val].key != key):
            hash_val = self.rehash(hash_val)

        if self.store[hash_val] is not None:
            result = self.store[hash_val].value
        else:
            result = None

        return result #Alternate: return None or self.store[hash_val].value

 
    def getKeys(self):
        return ([self.store[idx].key
                    for idx in range(len(self.store))
                         if self.store[idx] is not None])
 
    def __setitem__(self, key, value):
        hash_val = self.hash(key)

        if (self.store[hash_val] is not None
                and key == self.store[hash_val].key):
            self.store[hash_val].value = value
        else:
            while self.store[hash_val] is not None:
                hash_val = self.rehash(hash_val)
            self.store[hash_val] = Node(key, value)
            self.count += 1
            self.check_load()
 
    def hash(self, key):
        the_sum = sum([ord(ch) for ch in key])
        return the_sum % self.store_size

    def rehash(self, hash_val):
        return (hash_val + 1) % self.store_size

    def check_load(selfs):
        """
        compare count to store_size regaurding the Load_factor
        resize if needed
        :return:
        """
        pass
 
def read_file():
    fstr = "words_alpha.txt"
    fhandle = open(fstr)
    words = fhandle.read()
    words = words.split('\n')
    print("words length:", len(words))
    for word in words[:10]:
        print(word)
 
 
ht = HashTable(5)
ht["one"] = 1
ht["two"] = 2
ht["three"] = 3
ht["four"] = 4
ht["five"] = 5
ht["one"] = -1
print(ht)
print(ht.getKeys())
print(ht["one"])
print(ht["two"])
print(ht["three"])
 
#read_file()
























