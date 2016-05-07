__author__ = 'Hinshitsu-IT'
'''
5
10
25
3
0
1

1
2
0
1
1
'''
from math import sqrt
from itertools import combinations
number = 10
sqrt_number = int(sqrt(number))
# print(sqrt_number)
number_string = ''
for i in range(0,sqrt_number+1):
    number_string = number_string + str(i)
# print(number_string)
count = 0
for p in combinations(number_string,2):
    a, b = p
    a , b = int(a), int(b)
    print(a, b)
    pr = a ** 2 + b ** 2
    print(pr)
    if pr == number:
        count += 1
print(count)
