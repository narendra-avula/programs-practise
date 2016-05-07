__author__ = 'Hinshitsu-IT'
'''
2
2 3
3 5

1
2
'''

import sys
if sys.version_info[0]>=3:
    raw_input=input

test=int(raw_input())
if test >= 1 and test<=100000 :
    for i in range(test):
        start, last = map(int, raw_input().split(" "))
        if (start >=1 and start <= 10**9) and (last >=1 and last <= 10**9):
            res = start
            for i in range(start+1,last+1):
                res =  res ^ i
            print(res)

