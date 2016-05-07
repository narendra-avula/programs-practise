__author__ = 'Hinshitsu-IT'
'''
3
353 575
238746 39857
890 231

829
527327
32
'''

for _ in range(int(input())):
    a,b = map(str, input().split())
    print(int(str(int(a[::-1])+int(b[::-1]))[::-1]))


