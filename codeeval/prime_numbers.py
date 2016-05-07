__author__ = 'Hinshitsu-IT'
'''

'''
numbers = []
def prime_number(n):
    for num in range(2,n):
       # prime numbers are greater than 1
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               numbers.append(num)
prime_number(100)
print(numbers)

