__author__ = 'Hinshitsu-IT'

fhand = open('swap_case.txt','r')
for line in fhand:
    print(line.strip().swapcase())