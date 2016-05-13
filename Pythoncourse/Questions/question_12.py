__author__ = 'Kalyan'

# rotate the input list by number times in place.
# don't use any new intermediate lists if possible.
def rotate_right(input, number):
    pass

def test_rotate():
    input = range(1,7)
    rotate_right(input, 2)
    assert [5,6,1,2,3,4] == input

    input = range(1,7)
    rotate_right(input, 3)
    assert [4,5,6,1,2,3] == input

    input = range(1,7)
    rotate_right(input, 1)
    assert [6,1,2,3,4,5] == input




