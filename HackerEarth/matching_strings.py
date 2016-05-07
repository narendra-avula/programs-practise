__author__ = 'Hinshitsu-IT'
'''
4
TICK
TOCK
CAT
DOG
APPLE
APPLES
FANTASTIC
ANTASTIC

3
0
5
0
'''
for _ in range(int(input())):
    a = list(input())
    b = list(input())
    count = 0
    for i, j in zip(a, b):
        if i == j:
            count += 1
    print(count)