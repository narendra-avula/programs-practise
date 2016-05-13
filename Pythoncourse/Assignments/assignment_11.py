__author__ = 'Kalyan'

from treeutils import *
from placeholders import *

# can be used to fill up the tree with -1's
def init_func(node):
    node.value = -1

def weight_func(node):
    pass


def height_func(node):
    pass


def depth_func(node):
    pass


def balance_func(node):
    pass




# can be used to gather the node values as various nodes are visited
# useful for testing purposes.
class Accumulator(object):
    def __init__(self):
        self.result = []

    def visit(self, node):
        self.result.append(node.value)


# get the node values in order as a list.
def get_in_order(root):
    a = Accumulator()
    in_order(root, a.visit)
    return a.result

def get_pre_order(root):
    a = Accumulator()
    pre_order(root, a.visit)
    return a.result

#if you need state, you can use a class to hold state throughout the traversal
class Counter():
    def __init__(self):
        self.count = 0

    def visit(self, node):
        self.count += 1

def get_node_count(root):
    c = Counter()
    in_order(root, c.visit)
    return c.count

#for stateful solutions, you can write a helper function like get_node_count which extracts the state from the visitor class.
def test_node_count():
    input = (12, (30, 40, 50), (50, 60, None))
    root = create_tree(input)
    assert 6 == get_node_count(root)



def test_weight():
    input = (12, (30, 40, 50), (50, 60, None))
    root = create_tree(input)
    # invoke your weight func with the correct traversal below.
    #invoke_here.
    assert [1, 3, 1, 6, 1, 2] == get_in_order(root)

def test_height():
    input = (12, (30, 40, 50), (50, 60, None))
    root = create_tree(input)
    # invoke your height func with the correct traversal below.

    assert [2, 1, 0, 0, 1, 0] == get_pre_order(root)

# fill up the body
class BstChecker(object):
    pass


def is_bst(root):
    #fill me up
    pass

def test_is_bst():
    input = (12, (30, 40, 50), (50, 60, None))
    root = create_tree(input)

    assert False == is_bst(root)

    input = (100, (60, 40, 70), (120, 110, None))
    root = create_tree(input)
    assert True == is_bst(root)

def test_balance():
    input = (12, (30, 40, 50), (50, (60, 70, None), None))
    root = create_tree(input)
    # u need a 2 pass solution solution here! so call a traversal + visit funcs 2 times (which traversal and which visit each time?)

    assert [-1, 0, 0, 0, 2, 1, 0] == get_pre_order(root)

def test_depth():
    input = (12, (30, 40, 50), (50, (60, 70, None), None))
    root = create_tree(input)
    # same as comments as above


    assert [0,1,2,2,1,2,3] == get_pre_order(root)


three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___




