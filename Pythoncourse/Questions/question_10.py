__author__ = 'Kalyan'

def left_binary_search(input, value):
    pass


def test_left_binary_search():
    input = range(10)
    for index, value in enumerate(input):
        assert index == left_binary_search(input, value)
        
    assert -1 == left_binary_search(input, -10)
    assert -1 == left_binary_search(input, 100)

    assert -1 == left_binary_search([], 10)
    assert -1 == left_binary_search(None, 10)
    assert 0 == left_binary_search([10], 10)
    assert -1 == left_binary_search([10], 5)

    input = [1,1,2,2,2]

    assert 0 == left_binary_search(input, 1)
    assert 2 == left_binary_search(input, 2)
