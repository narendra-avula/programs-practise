__author__ = 'Hinshitsu-IT'
'''
3
120
121
231

The streak lives still in our heart!
The streak is broken!
The streak is broken!
'''
for _ in range(int(input())):
    number = int(input())
    if '21' not in str(number) and number % 21 != 0:
        print('The streak lives still in our heart!')
    else:
        print('The streak is broken!')