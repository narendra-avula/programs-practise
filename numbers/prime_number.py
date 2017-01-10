__author__ = 'narendra'

def isprime(number):
    if number == 2:
        return True
    if number == 3:
        return True
    if number % 2 == 0:
        return False
    if number % 3 == 0:
        return False

    start = 5
    interval = 2

    while start * start <= number:
        if number % start == 0:
            return False

        start += interval
        interval = 6 - interval

    return True

print isprime(69)