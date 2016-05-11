__author__ = 'CustomFurnish'
'''
Sample input:
4
1
2
5
3

Sample output:
1
2
120
6
'''

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# def factorial(n):
#     if n < 2:
#         return 1
#     return n * factorial(n - 1)
#
# print(factorial(1000))

from math import factorial
for _ in range(int(input())):
    number = int(input())
    print(factorial(number))