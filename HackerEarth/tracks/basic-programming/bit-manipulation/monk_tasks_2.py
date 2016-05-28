__author__ = 'Hinshitsu-IT'
'''
1
4
3 4 7 10

4 3 10 7
'''


# print(bin(7)[2:].count('1'))
from collections import defaultdict
import sys
if sys.version_info[0]>=3:
    raw_input=input

def countsetbits(n):
	setbits=0
	while n:
		n&=(n-1)
		setbits+=1
	return setbits

for _ in range(int(input())):
	s=[0]*100
	for i in range(100):
		s[i]=[]
	n=int(raw_input())
	l=[int(i) for i in raw_input().split()]
	for i in l:
		setb=countsetbits(i)
		s[setb].append(i)
	for i in range(100):
		if(len(s[i])>0):
			for j in s[i]:
				print(j,end=' ')
	print