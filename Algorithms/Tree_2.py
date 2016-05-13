__author__ = 'CustomFurnish'

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
print()
# l = getLeftChild(r)
# print(l)
# r = getRightChild(r)
# print(r)
# print()
# setRootVal(l,9)
# print(r)
# insertLeft(l,11)
# print(r)
# print(getRightChild(getRightChild(r)))

# x = BinaryTree('a')
# insertLeft(x,'b')
# insertRight(x,'c')
# insertRight(getRightChild(x),'d')
# insertLeft(getRightChild(getRightChild(x)),'e')
# print(x)