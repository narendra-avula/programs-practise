__author__ = 'Hinshitsu-IT'

import sys
if sys.version_info[0]>=3:
    raw_input=input


from math import factorial
def nCr(n,r):
    f = factorial
    return f(n) / f(r) / f(n-r)

test=int(raw_input())

if test >= 1 and test<=100000 :
    for i in range(test):
        girls, boys = map(int, raw_input().split(" "))
        if (girls >=1 and girls <= 50) and (boys >=1 and boys <= 50):
            print(int(nCr(girls+1,boys) * factorial(girls) * factorial(boys)))


