__author__ = 'narendra'


'''
This time your task is simple.

Given two integers
X
X and
K
K, find the largest number that can be formed by changing digits at atmost
K
K places in the number
X
X.

Input:

First line of the input contains two integers
X
X and
K
K separated by a single space.

Output:

Print the largest number formed in a single line.

Constraints:
SAMPLE INPUT
4483 2
SAMPLE OUTPUT
9983
Explanation
First two digits of the number are changed to get the required number.

'''

number, digits = map(int, raw_input().split())
numbers = [int(i) for i in str(number)]
count = 0
while digits > 0:
    if numbers[count] == 9:
        pass
    else:
        numbers[count] = 9
        digits -= 1
    count += 1
print ''.join(str(j) for j in numbers)