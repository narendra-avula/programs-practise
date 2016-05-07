__author__ = 'Hinshitsu-IT'
'''
1
7
22

1
1
0
'''

test_cases = open('happy_numbers.txt','r')
for test in test_cases:
    number = int(test.strip())
    print(number)

    digits = [int(i) for i in str(number)]
    print(digits)

    sum_square_digits = [int(i**2) for i in digits]
    print(sum_square_digits)

