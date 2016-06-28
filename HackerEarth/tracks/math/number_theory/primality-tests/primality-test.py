__author__ = 'Narendra'
'''
Given an integer(
N
N), write a code to check if it is prime or not.

Input Format:
First line has an integer
T
T - number of test cases.
Each test case is in a new line with a single integer
N
N.

Output Format:
Print "prime" if
N
N is prime, "composite" if
N
N is not a prime. Answer for each test case should be printed in a new line.

Constraints:

2
?
T
?
100
2?T?100
1
?
N
?
10
16
1?N?1016
SAMPLE INPUT
5
13
9
27
325
23

SAMPLE OUTPUT
prime
composite
composite
composite
prime
'''

def prime_check(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

for _ in range(int(raw_input())):
    number = int(raw_input())
    if prime_check(number):
        print "prime"
    else:
        print "composite"