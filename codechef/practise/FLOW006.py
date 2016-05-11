__author__ = 'CustomFurnish'
'''
All submissions for this problem are available.

You're given an integer N. Write a program to calculate the sum of all the digits of N.
Input

The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.
Output

Calculate the sum of digits of N.
Constraints

1 ? T ? 1000
1 ? N ? 100000
Example

Input
3
12345
31203
2123
Output
15
9
8
'''
def sum_of_digits(n):
    sum = 0
    while(n > 0):
        sum += n % 10
        n //= 10
    return sum

for _ in range(int(input())):
    print(sum_of_digits(int(input())))