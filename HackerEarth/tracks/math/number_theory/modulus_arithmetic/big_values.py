__author__ = 'Naidu'
'''
Arjun is a very good coder, but he is afraid of big numbers. He couldn't understand how to solve the questions with large numbers. And now he's stuck in a new question. Can you help him...

Given a number N, you just need to calculate C(N,6), where C(n,r) is the no. of combinations of r items from n items. C(n,r) = n!/(r! * (n-r)!) where n! = 1 * 2 * 3 * ... * n and 0! = 1

6<=N<10^6

Since, the value computed would be very large, print your answer in mod 10^9 + 7

Input:

First and only line of input will take an integer N.

Output:

Print C(N,6) mod 10^9 + 7

SAMPLE INPUT
6
SAMPLE OUTPUT
1
Explanation
C(6,6) = 6!/(6! * (6-6)!) = 6!/(6! * 0!) = 1
'''

# from math import factorial

def factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact *= i
    return fact

def combination(n,r):
    return factorial(n)/ ( factorial(r) * (factorial(n-r)) )

number = int(raw_input())
print combination(number, 6) % (10**9+7)


# print factorial(52009)
# print combination(6,4)