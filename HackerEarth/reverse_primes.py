__author__ = 'Hinshitsu-IT'
'''

'''
import sys
if sys.version_info[0]>=3:
    raw_input=input

def sieve(limit):
    isPrime = [True]*limit
    for i in range(2,limit):
        if isPrime[i]:
            j = 2
            while i*j < limit:
                isPrime[i*j] = False
                j += 1
    return isPrime
def isPalindrome(i):
    n = str(i)
    return n == n[::-1],int(n[::-1])

res = sieve(10**6)
for i in range(2,10**6):
    if res[i]:
        if not isPalindrome(i)[0]:
            print (i)
            res[isPalindrome(i)[1]] = False