__author__ = 'Narendra Avula'


def bubble_sort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist


alist = [12, 5, 7, 18, 11, 6, 12, 4, 17, 1]
bubble_sort(alist)
print(alist)