__author__ = 'Narendra Avula'

#still broken 'quicksort'

def partition(array):
    pivot = array[0]
    i = 1
    for j in range(i, len(array)):
        if array[j] < array[i]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i += 1
    array[0] = array[i]
    array[i] = pivot
    return array[0:(i)], pivot, array[(i+1):(len(array))]

def quick_sort(array):
    if len(array) <= 1: #if i change this to if len(array) == 1 i get an index out of bound error
        return array

    low, pivot, high = partition(array)
    #quick_sort(low)
    #quick_sort(high)

    return quick_sort(low) + [pivot] + quick_sort(high)

array = [5,3,4,2,7,6,1]

print (quick_sort(array))
# prints [1,2,3,5,4,6,7]