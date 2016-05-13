__author__ = 'Kalyan'

def right_binary_search(input, value):
    pass


def test_right_binary_search():
    input = range(10)
    for index, value in enumerate(input):
        assert index == right_binary_search(input, value)
        
    assert -1 == right_binary_search(input, -10)
    assert -1 == right_binary_search(input, 100)

    assert -1 == right_binary_search([], 10)
    assert -1 == right_binary_search(None, 10)
    assert 0 == right_binary_search([10], 10)
    assert -1 == right_binary_search([10], 5)

    input = [1,1,2,2,2]

    assert 1 == right_binary_search(input, 1)
    assert 4 == right_binary_search(input, 2)
