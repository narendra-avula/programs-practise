__author__ = 'Hinshitsu-IT'
'''
3
1
6
12

LB
SL
BS
'''
def cal(d):
	summ=0
	num=0
	N=1
	while summ<d:
		summ+=N
		num=N
		N=N+1
		if summ==d:
			return num
	return num

places =["SL","LB","BS"]
for i in range(int(input())):
	ans=cal(int(input()))
	print(places[ans%3])