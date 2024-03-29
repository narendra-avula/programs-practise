__author__ = 'Hinshitsu-IT'
'''
2
3
10

5
29
'''
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

numbers = ([2] + [i*2+1 for i, v in enumerate(sieve_for_primes_to(10000020)) if v and i>0])
# print(numbers)
# print(numbers[664579])
for _ in range(int(input())):
    print(numbers[int(input())-1])