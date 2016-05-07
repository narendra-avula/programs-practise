__author__ = 'Hinshitsu-IT'
'''
5 2
1 5 3 4 2

3
'''

number, difference = map(int, input().split())

numbers = map(int, input().split())
count = 0
for i in numbers:
    n = i
    print(n)
    for j in numbers:
        if abs( j - n )  == difference :
            count += 1
    print(count)
