__author__ = 'Narendra Avula'


def binary_search(alist, search_element):
    first  = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        middle = (first + last) // 2
        if alist[middle] == search_element:
            found = True
        elif alist[middle] < search_element:
            first = middle + 1
        else:
            last = middle - 1

    return found


alist = [2, 5, 7, 12, 14, 21, 28, 31, 36]
search_element = 22
print(binary_search(alist, search_element))