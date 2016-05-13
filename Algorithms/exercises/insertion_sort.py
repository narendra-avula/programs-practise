__author__ = 'Narendra Avula'

def insertion_sort(alist):
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index

        while position > 0  and alist[position-1] > current_value:
            alist[position] = alist[position-1]
            position -= 1

        alist[position] = current_value

    return alist

alist = [12, 5, 7, 18, 11, 6, 4, 17, 1]
insertion_sort(alist)
print(alist)