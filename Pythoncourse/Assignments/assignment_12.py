__author__ = 'Kalyan'

notes = '''
This assignment deals with tree creation from traversals.
'''

from placeholders import  *
from treeutils import *

def create_tree_pre_in(preorder, inorder):
    pass


def create_tree_post_in(postorder, inorder):
    pass


def create_tree_level_in(levelorder, inorder):
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

def get_post_order(root):
    a = Accumulator()
    post_order(root, a.visit)
    return a.result

def test_create_tree_pre_in():
    pre_list = [10, 20, 30, 40, 50, 60]
    in_list = [20, 10, 50, 40, 60, 30]

    root = create_tree_pre_in(pre_list, in_list)
    assert [20,50,60,40,30, 10] == get_post_order(root)


def test_create_tree_post_in():
    post_list = [20,50,60,40,30, 10]
    in_list = [20, 10, 50, 40, 60, 30]
    root = create_tree_post_in(post_list, in_list)
    assert [10, 20, 30, 40, 50, 60] == get_pre_order(root)


def test_create_tree_level_in():
    level_list = [10, 20, 30, 50, 40, 60, 70]
    in_list = [20, 10, 50, 30, 60, 40, 70]

    root = create_tree_level_in(level_list, in_list)
    assert [10, 20, 30, 50, 40, 60, 70] == get_pre_order(root)


three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___




