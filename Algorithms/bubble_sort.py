__author__ = 'CustomFurnish'

def bubble_sort(alist):
    for passnum in range(len(alist)-1,0,-1):
        print('Pass num = {}'.format(passnum))
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
        print(alist)

alist = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
print(alist)
bubble_sort(alist)
print(alist)
