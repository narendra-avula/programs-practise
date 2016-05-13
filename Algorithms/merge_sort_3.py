__author__ = 'Narendra Avula'

def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(L):
    print('---')
    print('mergesort on {}'.format(L))
    if len(L) < 2:
        print('length is 1: returning the list withouth changing')
        return L
    middle = int( len(L) / 2 )
    print('calling mergesort on {}'.format(L[:middle]))
    left = mergesort(L[:middle])
    print('calling mergesort on {}'.format(L[middle:]))
    right = mergesort(L[middle:])
    print('Merging left: {} and right: {}'.format(left,right))
    out = merge(left, right)
    print('exiting mergesort on {}'.format(L))
    print('#---')
    return out



print(mergesort([6,5,4,3,2,1]))