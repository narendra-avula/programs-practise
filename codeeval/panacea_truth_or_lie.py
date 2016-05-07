__author__ = 'Narendra'

def sum_hex_numbers(numbers):
    return sum(int(n, 16) for n in numbers)

def sum_binary_numbers(numbers):
    return sum(int(n, 2) for n in numbers)

test_cases = open('panacea_truth_or_lie.txt', 'r')
for test in test_cases:
    test = test.strip().split('|')
    hex_numbers = test[0].strip().split(' ')
    binary_numbers = test[1].strip().split(' ')
    if sum_hex_numbers(hex_numbers) == sum_binary_numbers(binary_numbers):
        print True
    else:
        print False