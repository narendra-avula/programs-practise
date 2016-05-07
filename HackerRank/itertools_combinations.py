__author__ = 'Hinshitsu-IT'

'''
HACK 2

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''


from itertools import combinations
a,b=input().split()
for i in range(1,int(b)+1):
    for e in combinations(sorted(a),i):
        print(''.join(e))
