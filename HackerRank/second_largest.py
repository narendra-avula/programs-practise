__author__ = 'Hinshitsu IT'

int(input())
a = list(set(map(int,input().split())))
#print(a)
a.sort()
print(a[-2])
