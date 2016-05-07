__author__ = 'Hinshitsu-IT'
'''
7
3 1 14 7 6 7 2

2 6 14
7 7 3 1
'''
n = int(input())
numbers = list(map(int,input().split()))
even = []
odd = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(' '.join(str(i) for i in sorted(even)))
print(' '.join(str(i) for i in sorted(odd,reverse=True)))