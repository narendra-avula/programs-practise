__author__ = 'Naidu'
'''
Sorry folks,, admin has no time to create a story for this problem...

You have two integers n and m and you have to print value of factorial(n)%m.

OUTPUT a single integer containing answer of problem.

Input 23 14567

NOTE You do not need to create a program for this problem you have to write your answers of given input in given code snippet

To see how to submit solution please check this link
SAMPLE INPUT
5 11
SAMPLE OUTPUT
10
'''

def factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact *= i
    return fact

n, m = map(int, raw_input().split())
print factorial(n) % m