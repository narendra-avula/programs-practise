__author__ = 'Narendra Avula'


def short_bubble_short(alist):
    exchanges = True
    passnum = len(alist) - 1
    count = 0

    while passnum > 0  and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                count += 1
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum -= 1
    return alist, count

alist = [12, 5, 7, 18, 11, 6, 12, 4, 17, 1]
result, count = short_bubble_short(alist)
print(result)
print('Total exchanges are {}'.format(count))