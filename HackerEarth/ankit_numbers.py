__author__ = 'Hinshitsu-IT'
'''
1
3

24
'''

from itertools import combinations

def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return int(sum)

for _ in range(int(input())):
    number = int(input())
    string = [str(i) for i in range(1,number+1)]
    for number in string:
        input_string = ''.join(str(x) for x in string)
        length = len(input_string)
    # print(input_string)
    # print(length)
    input_list = []
    for i in range(1,length+1):
        for e in combinations(input_string,i):
            input_list.append(''.join(e))
    # print(input_list)
    sum = 0
    for i in input_list:
        sum += sum_digits(int(i))
    print(sum)

    # input_string = ''.join(str(x) for x in string)
    # length = len(input_string)

# input_list = []
# for i in range(1,length+1):
#     for e in combinations(input_string,i):
#         input_list.append(''.join(e))
# sum = 0
# for i in input_list:
#     sum += sum_digits(int(i))
# print(sum)