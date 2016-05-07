__author__ = 'Hinshitsu-IT'

'''
vgxgp
3
2 4
2 5
7 14

Yes
No
Yes
'''

string = input()
for _ in range(int(input())):
    a, b = map(int, input().split())
    a = a % len(string)
    b = b % len(string)
    if string[a-1] == string[b-1]:
        print('Yes')
    else:
        print('No')