__author__ = 'Hinshitsu-IT'
'''
3
2
3
4

Yes
No
Yes
'''
for t in range(int(input())):
	n=int(input())
	print ("No" if n&n-1 else "Yes")


