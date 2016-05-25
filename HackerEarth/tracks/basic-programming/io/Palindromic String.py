__author__ = 'Naidu'
'''
You have been given a String
S
S. You need to find and print whether this string is a palindrome or not. If yes, print "YES" (without quotes), else print "NO" (without quotes).

Input Format
The first and only line of input contains the String
S
S. The String shall consist of lowercase English alphabets only.

Output Format
Print the required answer on a single line.

Constraints
1
?
|
S
|
?
100
1?|S|?100

Note
String
S
S consists of lowercase English Alphabets only.

SAMPLE INPUT
aba

SAMPLE OUTPUT
YES
'''

string = raw_input()
if string == string[::-1]:
    print "YES"
else:
    print "NO"

print "YES" if string == string[::-1] else "NO"