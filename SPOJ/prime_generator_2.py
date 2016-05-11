__author__ = 'Hinshitsu-IT'
'''
2
1 10
3 5

'''
import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False;
    return n>1;


for _ in range(int(input())):
    start, end = map(int, input().split())
    for n in range(start, end+1):
        if isPrime(n):
            print (n)
    print(end='\n')