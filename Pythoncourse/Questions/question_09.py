__author__ = 'Kalyan'


def binary_search(input, key):
    pass



def test_binary_search():
    input = range(10)
    for index, value in enumerate(input):
        assert index == binary_search(input, value)

    assert -1 == binary_search(input, -10)
    assert -1 == binary_search(input, 100)

    assert -1 == binary_search([], 10)
    assert -1 == binary_search(None, 10)
    assert 0 == binary_search([10], 10)
    assert -1 == binary_search([10], 5)


