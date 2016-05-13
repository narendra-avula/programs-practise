__author__ = 'Narendra Avula'
'''

'''
def merge(left, right):
    result = []
    i = 0
    j = 0

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

def merge_sort(L):
    if len(L) < 2:
        return L
    middle = int( len(L) // 2 )
    left = merge_sort(L[:middle])
    right = merge_sort(L[middle:])

    out = merge(left, right)

    return out

alist = [6,5,4,3,2,1]
print(merge_sort(alist))
