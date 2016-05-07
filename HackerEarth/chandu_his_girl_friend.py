__author__ = 'Hinshitsu-IT'
'''
2
5
2 5 2 4 3
5
5 4 2 3 1

5 4 3 2 2
5 4 3 2 1
'''
for _ in range(int(input())):
    n = int(input())
    print(' '.join(str(i) for i in sorted([(int(x)) for x in input().split()] ,reverse=True)))
