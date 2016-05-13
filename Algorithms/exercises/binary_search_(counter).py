__author__ = 'Narendra Avula'


def binary_search(alist, search_element):
    first  = 0
    last = len(alist)-1
    found = False
    count = 0

    while first <= last and not found:
        middle = (first + last) // 2
        count += 1
        if alist[middle] == search_element:
            found = True
        elif alist[middle] < search_element:
            first = middle + 1
        else:
            last = middle - 1

    return found, middle, count


alist = [2, 5, 7, 12, 14, 21, 28, 31, 36]
search_element = 21
found, index, count = binary_search(alist, search_element)

if found:
    print('Element is found at {} index in {} searches'.format(index, count))
else:
    print('Element not found . Total searches are {}'.format(count))