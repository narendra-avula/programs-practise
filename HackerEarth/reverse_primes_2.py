__author__ = 'Hinshitsu-IT'
'''

'''
import sys
if sys.version_info[0]>=3:
    raw_input=input

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            sieve[i+val::val] = [0]*tmp
    return sieve

numbers = ([2] + [i*2+1 for i, v in enumerate(sieve_for_primes_to(10**6)) if v and i>0])
# print(numbers)

def is_palindrome(i):
    n = str(i)
    return n == n[::-1],int(n[::-1])

for i in numbers:
    if not is_palindrome(i):
        print(i)