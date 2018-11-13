def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

def inorder2(root, spc=['-'] * 5):
    #spc = spc + ' '
    #spc.pop()
    #spc = ['-'] * 5
    #spc.append('-')
    if len(root) > 1:
        print(' '.join(spc), root[0])
        #spc.pop()
        inorder(root[1], poplist(spc))
        #print(spc, root[0])
        #spc2.append('-')
        inorder(root[2], appendlist(spc))
        #print(spc, root[0])
        #spc = spc + ' '

def inorder(root, level=0):
    level += 1
    if len(root) > 1:
        inorder(root[1], level)
        print(' '.join(['-'] * (20 - level)), root[0])
        inorder(root[2], level)


def getlevel(root, level=0):
    #print(level)
    level += 1
    if len(root) > 1:
        getlevel(root[1], level)
        getlevel(root[2], level)
    #print(level)
    #level += 1
    return level

def poplist(lst):
    lst.pop()
    return lst

def appendlist(lst):
    lst.append('-')
    lst.append('-')
    return lst

r = BinaryTree(3)
print(r)
insertLeft(r,4)
print(r)
insertLeft(r,5)
print(r)
insertRight(r,6)
print(r)
insertRight(r,7)
print(r)
l = getLeftChild(r)
print(l)
insertLeft(l, 55)

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))
insertRight(getLeftChild(r), 10)
print(r)
print(getlevel(r))
inorder(r)
