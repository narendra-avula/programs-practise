__author__ = 'Hinshitsu-IT'

'''
 1 2
 3 4

(1, 3) (1, 4) (2, 3) (2, 4)

'''

from itertools import product
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))

a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(' '.join(str(e) for e in product(a,b)))