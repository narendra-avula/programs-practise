__author__ = 'narendra'

def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

number = 2 ** 1000
print sum_digits(number)