__author__ = 'Narendra Avula'


def bubble_sort(alist):
    count = 0
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
    return alist, count

# alist = [12, 5, 7, 18, 11, 6, 12, 4, 17, 1]
alist = [6,5,4,3,2,1]
result , count = bubble_sort(alist)
print(result)
print('Total exchanges are {}'.format(count))