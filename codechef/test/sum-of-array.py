__author__ = 'narendra'


def sum_of_array(array):
    sum = 0
    for i in array:
        sum += i
    return sum

for _ in range(int(input())):
    len_number = int(input())
    numbers = map(int, raw_input().split())
    print sum_of_array(numbers)