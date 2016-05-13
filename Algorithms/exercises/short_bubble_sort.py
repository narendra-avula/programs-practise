__author__ = 'Narendra Avula'


def short_bubble_short(alist):
    exchanges = True
    passnum = len(alist) - 1

    while passnum > 0  and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum -= 1
    return alist

alist = [12, 5, 7, 18, 11, 6, 12, 4, 17, 1]
result = short_bubble_short(alist)
print(alist)