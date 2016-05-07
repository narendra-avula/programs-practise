__author__ = 'Hinshitsu-IT'
'''
1
3

24
'''

result = []
for i in range(int(input())):
	number = int(input())
	if number == 1:
		result.append(1)
	else:
		result.append( number * (number + 1) * 2 ** (number - 2))

for i in result:
    print(i)