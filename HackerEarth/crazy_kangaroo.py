__author__ = 'Hinshitsu-IT'
'''
3
1 10 2
5 10 3
7 9 5

5
2
0
'''
for _ in range(int(input())):
    start, last, number = map(int, input().split())
    array = [i for i in range(start,last+1) if i % number == 0 ]
    print(len(array))