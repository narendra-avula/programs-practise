__author__ = 'narendra'


def sum_of_digits(n):
    sum = 0
    while( n > 0 ):
        sum += n%10
        n /= 10
    return sum

for _ in range(int(input())):
    number = int(input())
    print sum_of_digits(number)