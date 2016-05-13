__author__ = 'Narendra Avula'

def insertion_sort(alist):
    count = 0
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index

        while position > 0  and alist[position-1] > current_value:
            alist[position] = alist[position-1]
            count += 1
            position -= 1

        alist[position] = current_value

    return alist, count

# alist = [12, 5, 7, 18, 11, 6, 12, 4, 17, 1]
alist = [6,5,4,3,2,1]
result, count = insertion_sort(alist)
print(result)
print('Total exchanges are {}'.format(count))
