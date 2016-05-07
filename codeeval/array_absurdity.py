__author__ = 'Hinshitsu-IT'
'''
5;0,1,2,3,0
20;0,1,10,3,2,4,5,7,6,8,11,9,15,12,13,4,16,18,17,14

0
4
'''
from collections import Counter
test_cases = open('array_absurdity.txt','r')
for test in test_cases:
    no_of_numbers, numbers  = test.strip().split(';')
    no_of_numbers = int(no_of_numbers)
    numbers = [int(i) for i in numbers.split(',')]
    # print(no_of_numbers, numbers)
    print(''.join(str(i) for i in [k for k,v in Counter(numbers).items() if v>1]))
