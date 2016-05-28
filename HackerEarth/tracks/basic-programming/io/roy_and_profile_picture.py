__author__ = 'Hinshitsu-IT'

'''
180 len
3  num
640 480     dim1
120 300     dim2
180 180     dim3

CROP IT
UPLOAD ANOTHER
ACCEPTED
'''
import sys
if sys.version_info[0]>=3:
    raw_input=input

length = int(raw_input())
for _ in range(int(raw_input())):
    width, height = map(int,raw_input().split())
    if width < length or height < length :
        print ("UPLOAD ANOTHER")
    elif width == height:
        print('ACCEPTED')
    else:
        print('CROP IT')