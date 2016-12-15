__author__ = 'narendra'


# def array_left_rotation(array, rotation):
#     return  ' '.join(str(x) for x in array[rotation:] + array[:rotation])
#
# array_length, rotation = map(int, raw_input().split())
# array_list = map(int, raw_input().split())
# print array_left_rotation(array_list, rotation)

def array_left_rotation(array, rotation):
    return  ' '.join(str(x) for x in array[rotation:] + array[:rotation])

array_length, rotation = map(int, raw_input().split())
array_list = map(int, raw_input().split())
print array_left_rotation(array_list, rotation)