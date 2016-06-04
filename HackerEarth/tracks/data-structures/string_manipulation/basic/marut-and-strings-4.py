__author__ = 'Naidu'
'''
Marut loves good strings. According to him, good strings are those which contain either all alphabets of uppercase or lowercase. While he is preparing for his exams, he finds many bad strings in his book and wants to convert them to good strings. But he wants to do this in minimum number of operations.
In one operation, he can pick only one character of any case and convert it to any other case.

As his exams are going on, he wants your help.

Input:
The first line contains an integer T, denoting the number of test cases.
Each test case consists of only one line with a string S which contains uppercase and lowercase alphabets..

Output:
Print the minimum number of operations, in which Marut can obtain a good string.
Print the answer for each test case in new line.

Constraints:
1 ? T ? 10
If T is not in this range, print "Invalid Test" (without the quotes)
1 ? Length of S ? 100
S can contain numbers, special characters but no spaces.
If the length of string is not in the above range or it does not contain any alphabets, print "Invalid Input" (without the quotes)

For Example, if the input is:
0
TestString

Print "Invalid Test" (without the quotes)

SAMPLE INPUT
3
abcEfg
!@6#2
123A
SAMPLE OUTPUT
1
Invalid Input
0
'''

test_cases = int(raw_input())
while test_cases > 0:
    string = raw_input()
    alphabets_string = ''
    for i in string:
        if i.isalpha():
            alphabets_string += i
    lower_letters = 0
    upper_letters = 0
    for i in alphabets_string:
        if i.islower():
            lower_letters += 1
        else:
            upper_letters += 1
    if len(alphabets_string) == 0:
        print "Invalid Input"
    elif lower_letters > upper_letters:
        print upper_letters
    else:
        print lower_letters
    test_cases -= 1