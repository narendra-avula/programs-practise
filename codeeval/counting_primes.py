__author__ = 'Hinshitsu-IT'
'''
2,10
20,30

4
2

'''

def is_prime(n):
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True

test_cases = open('counting_primes.txt','r')
for test in test_cases:
    start, end = map(int, test.strip().split(','))
    result = [str(i) for i in range(start, end+1) if is_prime(i)]
    print(len(result))