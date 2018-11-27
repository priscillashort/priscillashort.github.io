class Stack:
    __init__(self):
        __lst =

def inorder(self):
    lst = []
    s = Stack()
    current = self.root

    if current is not None:
        s.push(current)

    done = current is None and s.is_empty()

    while not done:
        while current != None:
            current = current.leftChild
            if current is not None:
                s.push(current)

def my_reverse(lst):
    my_stack = Stack()
    for i in range(lst):
        my_stack.push(i)
    lst.clear()
    for j in range(my_stack):
        lst.append(my_stack.pop())

    return lst

ls = [10,9,8,7,6,5,4]

print(ls)

my_reverse(ls)

print(ls)