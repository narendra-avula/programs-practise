__author__ = 'Narendra Avula'

def qsort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        return qsort(less)+equal+qsort(greater)
    else:
        return array

array =[12,4,5,6,7,3,1,15]
print(qsort(array))

