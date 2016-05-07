__author__ = 'Hinshitsu-IT'
'''
10
20
100


'''

def is_prime(n):
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True

test_cases = open('prime_numbers.txt','r')
for test in test_cases:
    number = int(test)
    print(','.join(str(i) for i in range(2, number) if is_prime(i)))

