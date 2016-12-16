__author__ = 'narendra'

#
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# result =  str(factorial(1000))
# print result
# numbers =  [int(i) for i in result]
# print sum(numbers)

import math
import time
start_time = time.time()
result =  math.factorial(99999)
print result
print("--- %s seconds ---" % (time.time() - start_time))

