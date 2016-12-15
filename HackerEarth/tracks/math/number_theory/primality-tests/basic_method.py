__author__ = 'Narendra'

def prime_check(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print prime_check(100000000)