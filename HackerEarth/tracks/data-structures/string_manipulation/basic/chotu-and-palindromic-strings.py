__author__ = 'Naidu'
'''
Everyone knows that chotu likes palindromic strings. One day, he found 2 ordinary strings s1 and s2. Now he wonders if he could make a palindrome by concatenating s1 and s2 in any order. i.e if s1s2 or s2s1 is a palindrome.

Input
First line of input contains T, denoting number of test cases.
Each test case contains two lines, first line contains string s1 and second line contains string s2.

Output
Print T lines, either "YES" or "NO"(without quotes).

Constrains
1 <= T <= 1000
1 <= |s1|, |s2| <= 10000
Both strings contain only lower case letters.

SAMPLE INPUT
2
aba
baba
xy
zw

SAMPLE OUTPUT
YES
NO
'''
def palindrome(string):
    return string == string[::-1]

test_cases = int(raw_input())
while test_cases > 0:
    s1 = raw_input()
    s2 = raw_input()
    one = s1 + s2
    two = s2 + s1
    if palindrome(one) or palindrome(two):
        print "YES"
    else:
        print "NO"
    test_cases -= 1
