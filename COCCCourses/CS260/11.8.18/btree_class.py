import node

class BTree:

    def __init__(self):
        self.root = None
        self.data

    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        elif data < self.root.data():
            insert(self, data, )

    def __str__(self):
        return "[]"











if __name__ == "__main__":
    tree = BTree()
    print(tree)