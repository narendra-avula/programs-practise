__author__ = 'Naidu'
'''
Given a word consisting of lowercase English letters, write a program to remove duplicates from the word. The characters in the output must preserve the same order, as their first appearance in the original word.

Input Format

The input consists of several test cases.
The first line of the input file contains a positive integer T, the number of test cases.
Then, T lines follow, each containing a single word W (no spaces, only lowercase English letters).

Output Format

The output must contain exactly T lines, each line containing a single word, the required answer.

Constraints

1 ? T ? 100
1 ? |W| ? 31

SAMPLE INPUT
2
hello
world
mississippi

SAMPLE OUTPUT
helo
world
misp
'''

test_cases = int(raw_input())
while test_cases > 0:
    string = raw_input()
    new_string = ''
    for i in string:
        if i not in new_string:
            new_string += i
    print new_string
    test_cases -= 1