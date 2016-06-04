__author__ = 'Naidu'
'''
Given two numbers
N
N and
M
M, print the absolute difference between two numbers i.e.
|
N
?
M
|
|N?M|.
Approach:

Store the difference of
N
N and
M
M in a temporary variable result.
Check if result's value is negative, if it is then make it positive by mutiplying with
?
1
?1 because the question is asking for absolute difference.
Print out the value of result.
'''

a, b = map(int, raw_input().split())
difference = a - b
if difference < 0:
    difference = difference * (-1)
print difference