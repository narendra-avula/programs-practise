__author__ = 'Naidu'
'''
Everybody loves palindromes, but Artur doesn't.
He has a string S that consists of lowercase English letters ('a' - 'z'). Artur wants to find a substring T of S of the maximal length, so that T isn't a palindrome.

Input
The input contains a single line, containing string S. String S consists of lower case English letters.

Output
In a single line print the length of T

Constraints
1 ? |S| ? 100000

SAMPLE INPUT
aba
SAMPLE OUTPUT
2
'''

def palindrome(string):
    return string == string[::-1]

string = raw_input()
if len(set(list(string))) == 1:
    print 0
    quit()
if palindrome(string):
    print ( len(string)/2 ) + 1
else:
    print len(set(list(string)))