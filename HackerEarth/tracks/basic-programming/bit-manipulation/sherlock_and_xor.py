__author__ = 'Hinshitsu-IT'
'''
2
3
1 2 3
4
1 2 3 4

2
4
'''

import sys
if sys.version_info[0]>=3:
    raw_input=input

for _ in range(int(input())):
    n = int(input())
    numbers = [int(x) for x in input().split()]
    even, odd = 0, 0
    for item in numbers:
        if item % 2 == 0 :
            even += 1
        else:
            odd += 1
    print (str(even*odd))



