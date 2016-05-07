__author__ = 'Hinshitsu-IT'
'''
3
abcd
2
a c
aaaa
1
a
ababab
2
a b

6
0
0
'''
def weight(string):
	w = 0
	for i in string:
		w += ord(i) - 96
	return w

t = int(input())
for j in range(t):
	string = input()
	num  = int(input())
	chars = list(map(str, input().split(' ')))
	for i in range(num):
		string = string.replace(chars[i], '')
	print(weight(string))