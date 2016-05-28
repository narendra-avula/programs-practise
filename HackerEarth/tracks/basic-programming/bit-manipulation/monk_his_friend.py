__author__ = 'Hinshitsu-IT'
'''
4
1 4
3 3
5 1
8 7

2
0
1
4
'''

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(str(bin(a^b)).count('1'))