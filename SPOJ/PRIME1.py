__author__ = 'Narendra'

'''
Peter wants to generate some prime numbers for his cryptosystem. Help him! Your task is to generate all prime numbers between two given numbers!

Input

The input begins with the number t of test cases in a single line (t<=10). In each of the next t lines there are two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

Output

For every test case print all prime numbers p such that m <= p <= n, one number per line, test cases separated by an empty line.

Example

Input:
2
1 10
3 5

Output:
2
3
5
7

3
5
'''

def sieve(n):
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)

for _ in range(int(raw_input())):
    start, end = map(int, raw_input().split())
    prime_numbers = sieve(end)
    start_index = 0
    while True:
        if start in prime_numbers:
            start_index = start
            break
        else:
            start += 1
    final_start = prime_numbers.index(start_index)
    for i in range(final_start, len(prime_numbers)):
        print prime_numbers[i]