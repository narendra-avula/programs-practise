__author__ = 'narendra'

import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    sum = 0
    for num in range(2, 2000000):
        if is_prime(num):
            sum += num
            print(num)

    print sum

import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))