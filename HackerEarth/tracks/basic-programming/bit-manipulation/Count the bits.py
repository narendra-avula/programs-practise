__author__ = 'Naidu'
'''
Given a number
N
N, print the number of set bits in the binary representation of this number.

Input:
The first contains a single integer
T denoting the number of test cases. Each test case contains a single integer
N
N
Output:
For each test case, print a single integer denoting the number of set bits in the binary representation of the given
N
N .
'''

def count_set_bits(number):
    count = 0
    while (number):
        number = number & (number-1)
        count += 1
    return count

test_cases = int(raw_input())
while(test_cases > 0):
    number = int(raw_input())
    print count_set_bits(number)
    test_cases -= 1