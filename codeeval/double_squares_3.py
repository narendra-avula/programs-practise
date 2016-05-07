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

test_cases = open('double_squares.txt','r')
from math import sqrt
from itertools import combinations
test_file = [int(test.strip()) for test in test_cases]
for i in test_file[1:]:
    number = i
    number_string = [str(i) for i in range(0,int(sqrt(number))+1)]
    string = ''.join(number_string)
    count = 0
    for p in combinations(string,2):
        a, b = map(int, p)
        if a ** 2 + b ** 2 == number:
            count += 1
    print(count)




