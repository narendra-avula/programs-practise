__author__ = 'narendra'


pages_input = {
    1:[4,5,6],
    2:[5,6],
    5:[1,6,7]
}
final_dict = {}
pages_outs_list = []
for key, each_page_outs in pages_input.items():
    for out_lines in each_page_outs:
        out_combos = (key, out_lines)
        out_combos = out_combos[::-1]
        pages_outs_list.append(out_combos)
list_of_start_nodes= []
for each_out_combo in pages_outs_list:
    if each_out_combo[0] not in list_of_start_nodes:
        list_of_start_nodes.append(each_out_combo[0])
for each_data_tuple in pages_outs_list:
    if each_data_tuple[0] in list_of_start_nodes and not final_dict.get(each_data_tuple[0]):
        final_dict[each_data_tuple[0]] = list()
        final_dict[each_data_tuple[0]].append(each_data_tuple[0])
        final_dict[each_data_tuple[0]].append(each_data_tuple[1])
    else:
        final_dict[each_data_tuple[0]].append(each_data_tuple[1])
for key, value in final_dict.items():
    print value



# def get_outlinks(links):
#     final_dict = dict()
#     in_links = []
#     for key, value in links:
#         final_dict[key] = in_links.append(value)
#
#     print final_dict
#
#
# final_links = []
# pages = int(raw_input())
# for page in range(pages):
#     outlinks_tuple = []
#     outlinks = map(int, raw_input().split())
#     for id in range(len(outlinks)-1):
#         outlinks_tuple.append(( outlinks[id+1], outlinks[0] ))
#     final_links = final_links + outlinks_tuple
#
# print final_links
# get_outlinks(final_links)
# # print dict(final_links)




# def minimum_number(numbers):
#     min_num = None
#     for num in numbers:
#         if min_num is None:
#             min_num = num
#         elif num < min_num:
#             min_num = num
#     return min_num
#
#
# def maximum_number(numbers):
#     max_num = -1
#     for num in numbers:
#         if num > max_num:
#             max_num = num
#     return max_num
#
# def min_max_numbers(numbers):
#     min_num = max_num = numbers[0]
#     for num in numbers[1:]:
#         if num < min_num:
#             min_num = num
#         elif num > max_num:
#             max_num = num
#
#     return min_num, max_num
#
# numbers = map(int, raw_input().split())
# min_max_numbers =  min_max_numbers(numbers)
# print str( min_max_numbers[0] ) +" "+ str( min_max_numbers[1] )


# print minimum_number(numbers), maximum_number(numbers)



# foo = [1,2,3,'a', None, (), []]
# print len(foo)


# def strange(j):
#     k = 0
#     while j > 0:
#         k = 10 * k + j%10
#         j = j/10
#     return k
#
# print  strange(1230)
#
# def example(val):
#   val = val + '4'
#   val = val*2
#   return val
#
# print example("jump")


# def sum(x):
#     res = 0
#     for i in range(x):
#         res += i
# print(sum(10))

# try:
#   print(1)
#   assert 2 + 2 == 5
# except AssertionError:
#   print(3)
# except:
#   print(4)

# nums = [1,2,8,3,7]
# res = list(filter(lambda x:x%2==0, nums))
# print res


# try:
#     with open("text.txt") as f:
#         print(f.read())
# except:
#     print("Error")

# nums = {1, 2, 3, 4, 5, 6}
# nums = {0, 1, 2, 3} & nums
# print(nums)
# nums = filter(lambda x: x > 1, nums)
# print(nums)
# print(len(list(nums)))


# def power(x, y):
#   if y == 0:
#     return 1
#   else:
#     return x * power(x, y-1)
#
# print(power(2, 3))
#
#
# nums = (55, 44, 33, 22)
# print(max(min(nums[:2]), abs(-42)))













# x = 3
# print (17%3)
#
# while False:
#     print("Looping")

# def print_nums(x):
#     for i in range(x):
#         print (i)
#     return
# print( print_nums(10) )


# letters = ['x', 'y', 'z']
# letters.insert(1, 'w')
# print(letters[2])


# def func(x):
#     res = 0
#     for i in range(x):
#         res += i
#     return res
#
# print(func(4))

# for i in range(10):
#     if not i%2 == 0:
#         print i+1

# list = [1, 1, 2, 3, 5, 8, 13]
# print(list[list[4]])


# def min(x, y):
#   if x<=y:
#    return x
#   else:
#     return y


# x = 4
# x += 5
# print x

# spam = "7"
# spam = spam + "0"
# eggs = int(spam) + 3
# print(float(eggs))
#
# x = 5
# y = x + 3
# y = int(str(y) + "2")
# print y