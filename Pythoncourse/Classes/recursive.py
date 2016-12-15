__author__ = 'narendra'


# def max_number(arr):
#     largest = None
#     for i in arr:
#         if type(i) is int:
#             if (largest is None) or (largest < i):
#                 max_num = i
#                 # print i
#         elif type(i) is list:
#             max_number(i)
#
#     return largest
#
# array_list = [2,9,[1,10],5,6]
# print max_number(array_list)

def max_number(arr):
    largest = None
    first_time = True
    for num in arr:
        if type(num) is list:
            val = max_number(num)
        else:
            val = num

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest

array_list = [2,9,[1,10],5,6]
print max_number(array_list)