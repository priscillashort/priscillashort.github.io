from random import randint

def create_list(size):
    nums = set()

    while len(nums) < size:
        nums.add(randint(1,size*10))

    return nums

def insert(btree, num, root=0):
    if btree[root] == None:
        btree[root] = num
    elif num < btree[root]:
        insert(btree, num, root * 2 + 1)
    else:
        insert(btree, num, root * 2 + 2)

def inorder(btree, root=0):
    if btree[root] is not None:
        inorder(btree, root * 2 + 1)
        print(btree[root], end=',')
        inorder(btree, root * 2 + 2)

def preorder(btree, root=0):
    if btree[root] is not None:
        print(btree[root], end=',')
        inorder(btree, root * 2 + 1)
        inorder(btree, root * 2 + 2)

def postorder(btree, root=0):
    if btree[root] is not None:
        inorder(btree, root * 2 + 1)
        inorder(btree, root * 2 + 2)
        print(btree[root], end=',')



num_count = 20
nums = create_list(num_count)
print(nums)
btree = [None] * (num_count * 100)
for item in nums:
    insert(btree, item)

inorder(btree)
print()
preorder(btree)
print()
postorder(btree)

