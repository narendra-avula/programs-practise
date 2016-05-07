__author__ = 'Hinshitsu-IT'
'''
3
1 10 2
5 10 3
7 9 5

5
2
0
'''
test=int(input())
ans=[]
if test>=1 and test<=100000:
	for i in range(test):
		a,b,m=map(int, input().split(" "))
		c=0
		if (a>=1 and b<=10**12) and (b>=1 and b<=10**12):
			ans.append(abs((b/m)-((a-1)/m)))
	for res in ans:
		print(int(res))