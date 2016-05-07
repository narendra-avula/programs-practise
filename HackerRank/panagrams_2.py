__author__ = 'Hinshitsu-IT'
'''
2
We promptly judged antique ivory buckles for the next prize
We promptly judged antique ivory buckles for the prize

'''

import string
s = input().lower().strip()
if all(c in s for c in string.ascii_lowercase):
    print('pangram')
else:
    print('not pangram')
