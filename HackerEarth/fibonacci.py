__author__ = 'Hinshitsu-IT'

def fib(n):
    if n == 0: return 1
    elif n == 1: return 1
    else: return fib(n-1) + fib(n-2)

numbers = []
for i in range(1,34):
    if fib(i) % 2 == 0:
        numbers.append(fib(i))
print(sum(numbers))

