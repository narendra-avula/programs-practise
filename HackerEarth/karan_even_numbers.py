__author__ = 'Hinshitsu-IT'
'''
1 3 4 7 9 6 -1

4
6
'''
numbers = map(int, input().split())
for number in numbers:
    if number %2 == 0:
        print(number)
    if number == -1:
        quit()