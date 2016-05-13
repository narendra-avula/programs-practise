__author__ = 'Narendra Avula'

def short_bubble_sort(alist):
    print('start')
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum -= 1

alist=[20,30,40,90,50,60,70,80,100,110]
short_bubble_sort(alist)
print(alist)