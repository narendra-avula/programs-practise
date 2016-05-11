__author__ = 'CustomFurnish'
'''
All submissions for this problem are available.

If an Integer N, write a program to reverse the given number.
Input

The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.
Output

Display the reverse of the given number N.
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
54321
30213
3212
'''

def reverse(num):
  rev = 0
  while(num > 0):
    rev = (10*rev)+num%10
    num //= 10
  return rev

for _ in range(int(input())):
    print(reverse(int(input())))