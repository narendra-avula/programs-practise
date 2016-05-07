__author__ = 'Narendra'

def is_prime(n):
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True

def mersenne_prime(n):
    numbers = [3,7,31,127,8191,131071, 524287, 2147483647, 2305843009213693951 ]
    if n in numbers:
        return True
    return False

test_cases =  open('mersenne_prime.txt', 'r')
for test in test_cases:
    number = int(test)
    print(','.join(str(i) for i in range(2, number) if is_prime(i) if mersenne_prime(i) ))

