
import timeit
import random
import copy

"""
    Priscilla Short
    Add del as a function of the map (HashTable) ADT

    Description of Exercise:
    How can you delete items from a hash table that uses chaining for collision resolution? 
    How about if open addressing is used? What are the special circumstances that must be handled? 
    Implement the del method for the HashTable class.
"""

class HashTable:
    def __init__(self, tableSize=11):
        self.size = tableSize
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
        #if key in self:
            #return

        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #replace
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and \
                      self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
        return self.data[self.index(key)]

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def __contains__(self, key):
        return self.get(key) is not None

    def index(self,key):
        startslot = self.hashfunction(key,len(self.slots))
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and  \
                       not found and not stop:
            if self.slots[position] == key:
                found = True
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return position

    def get2(self,key):
        startslot = self.hashfunction(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and  \
                       not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __str__(self):
        #return str([(key, self.data[self.index(key)]) for key in self.slots if key is not None])
        #return str([(self.slots[self.index(thekey)], self.data[self.index(thekey)]) for thekey in self.slots if thekey != None])
        lst = []
        for i in self.slots:
            if i != None:
                #print(i)
                lst.append((i, self.get2(i)))
        return str(lst)
    #, self.data[self.index(key)

    def delete(self,key):
        idx = self.index(key)
        idx2 = copy.deepcopy(idx)
        #lst = [self.index(key)]
        self.data[idx2] = None
        self.slots[idx2] = None


if __name__ == "__main__":

    ht = HashTable()
    ht.put(1, "one")
    ht.put(12,"twelve")
    #ht.put(1,"test")
    print("ht:", ht)
    print("index of 1:", ht.index(1))
    print("index of 12:", ht.index(12))
    print("data of 1:", ht[1])
    print("data of 12:", ht[12])
    print("Deleting 12:")
    ht.delete(12)
    print("slots at index 2 after deleting 12:", ht.slots[2])
    print("data at index 2 after deleting 12:", ht.data[2])
    print("ht:", ht, '\n')

    print("        Timing index     Timing deleting")
    index = timeit.Timer("ht2[i]", "from __main__ import HashTable, ht2, i")
    delete = timeit.Timer("ht2.delete(i)", "from __main__ import HashTable, ht2, i")
    ht2 = HashTable(10000)
    for j in range(10000):
        ht2.put(j + random.randint(1,10000), str(j))
        #random.randint(1,10000)
    for i in range(10000): #[item for item in ht2.slots if item is not None]: #range(10001):
        timeIndex = index.timeit(number=100)
        timeDelete = delete.timeit(number=100)
        if (i % 500) == 0:
            print("%15.5f, %15.5f" %(timeIndex,timeDelete))
            #print("%15.5f" % (timeDelete))
    print('\n', ht2)


