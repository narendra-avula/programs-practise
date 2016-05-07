__author__ = 'Hinshitsu-IT'
'''
2
1 2

NO
'''

n=int(input())
A=list(map(int,input().split()))
if sum(A[0:n:2])==sum(A[1:n:2]):
	print("YES")
else:
	print("NO")