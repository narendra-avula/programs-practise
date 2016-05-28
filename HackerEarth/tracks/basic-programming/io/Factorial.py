__author__ = 'Naidu'
'''
You have been given a positive integer
N
N. You need to find and print the Factorial of this number. The Factorial of a positive integer
N
N refers to the product of all number in the range from
1
1 to
N
N. You can read more about the factorial of a number here.

Input Format:
The first and only line of the input contains a single integer
N
N denoting the number whose factorial you need to find.

Output Format
Output a single line denoting the factorial of the number
N
N.

Constraints
1
?
N
?
10
1?N?10

SAMPLE INPUT
2
SAMPLE OUTPUT
2
'''

number = int(raw_input())
fact = 1
for i in range(number):
    fact += fact * i
print fact

