__author__ = 'Hinshitsu-IT'
'''
Chandu is a bad student. Once his teacher asked him to print the reverse of a given string. He took three hours to solve it. The teacher got agitated at Chandu and asked you the same question. Can you solve it?

Input:
The first line contains an integer T, denoting the number of test cases.
Each test case contains a string S, comprising of only lower case letters.

Output:
For each test case, print the reverse of the string S.

Constraints:

1 <= T <= 10
1 <= |S| <= 30

SAMPLE INPUT
2
ab
aba

SAMPLE OUTPUT
ba
aba
'''
import sys
if sys.version_info[0]>=3:
    raw_input=input

for _ in range(int(raw_input())):
    print(raw_input()[::-1])