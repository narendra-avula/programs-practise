__author__ = 'Hinshitsu-IT'
'''
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10

 (5^2+9^2+10^2)%1000 = 206.

206
'''
#
# number_test_cases , modulus  = map(int,input().split())
# max_list = []
# for i in range(int(number_test_cases)):
#     input_string = input().split()
#     k = input_string[0]
#     input_list = [int(i) for i in input_string[1:]]
#     #print(k, input_list)
#     max_list.append(max(input_list))
#
# #print(max_list)
#
#
# sum = 0
# for item in max_list:
#     sum += item ** 2
# # print(sum)
# print(sum % int(modulus))
from itertools import product
K,M=map(int,input().split())
a=[[int(e)**2 for e in input().split()][1:] for _ in range(K)]
print(a)
print(max(sum(e)%M for e in product(*a)))