__author__ = 'narendra'


def fib(n):
    if n <= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t

import time
for n in range(1,10):
    start = time.clock()
    result = fib(n)
    end = time.clock()
    print("fib({0}) = {1}, ({2:.2f} secs)".format(n, result, end - start))