__author__ = 'CustomFurnish'
'''
All submissions for this problem are available.

Read problems statements in Mandarin Chinese , Russian and Vietnamese

A number is called palindromic if its decimal representation is a palindrome. You are given a range, described by a pair of integers L and R. Find the sum of all palindromic numbers lying in the range [L, R], inclusive of both the extrema.
Input

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a pair of space separated integers L and R denoting the range for which you are required to find the sum of the palindromic numbers.
Output

For each test case, output a single line containing the sum of all the palindromic numbers in the given range.
Constraints

1 ? T ? 100
Subtask 1 (34 points) : 1 ? L ? R ? 103
Subtask 2 (66 points) : 1 ? L ? R ? 105
Example

Input:
2
1 10
123 150

Output:
45
272

Explanation

Example case 1. The palindromic numbers between 1 and 10 are all numbers except the number 10. Their sum is 45.
Example case 2. The palindromic numbers between 123 and 150 are 131 and 141 and their sum is 272.
'''

# def is_palindrom(n):
#     s = str(n)
#     return s == s[::-1]

def reverse(num):
  temp = num
  rev = 0
  while(num > 0):
    rev = (10*rev)+num%10
    num //= 10
  return temp == rev

for _ in range(int(input())):
    start, end = map(int, input().split())
    sum = 0
    for i in range(start, end+1):
        if reverse(i):
            sum += i
    print(sum)