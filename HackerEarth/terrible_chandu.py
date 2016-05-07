__author__ = 'Hinshitsu-IT'
'''
2
ab
aba

ba
aba

'''
import sys
if sys.version_info[0]>=3:
    raw_input=input

for _ in range(int(raw_input())):
    print(raw_input()[::-1])