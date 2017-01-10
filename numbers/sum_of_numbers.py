__author__ = 'narendra'


def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def sum_of_numbers_2(numbers):
    return sum(numbers)