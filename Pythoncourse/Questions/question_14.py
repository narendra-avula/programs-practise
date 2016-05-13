__author__ = 'Kalyan'

from listutils import *


def merge_lists(head1, head2):
    pass


def test_merge_lists():
    head1 = to_linked_list([1, 2, 3])
    head2 = to_linked_list([1, 2, 3, 4, 5])

    result = merge_lists(head1, head2)
    assert [1, 1, 2, 2, 3, 3, 4, 5] == from_linked_list(result)

    head1 = to_linked_list([1, 2, 5])
    head2 = to_linked_list([4, 6, 7])

    result = merge_lists(head1, head2)
    assert [1, 2, 4, 5, 6, 7] == from_linked_list(result)

    head1 = to_linked_list([])
    head2 = to_linked_list([1, 2, 3, 4])

    result = merge_lists(head1, head2)
    assert [1, 2, 3, 4] == from_linked_list(result)

    result = merge_lists(None, None)
    assert [] == from_linked_list(result)






