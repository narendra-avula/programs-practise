__author__ = 'Hinshitsu-IT'
'''
aaabbbb

'''
from itertools import permutations
string = input()
perms = ["".join(perm) for perm in permutations(string)]
if string[::-1] in perms:
    print('YES')
    quit()
else:
    print('NO')
    quit()