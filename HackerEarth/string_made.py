__author__ = 'Hinshitsu-IT'

'''
12134

18

'''


import sys
if sys.version_info[0]>=3:
    raw_input=input

dashes = {0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
input_list = map(int,input())
print(sum(dashes[i] for i in input_list))