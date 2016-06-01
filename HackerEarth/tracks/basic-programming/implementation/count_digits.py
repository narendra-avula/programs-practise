__author__ = 'Naidu'
'''
You are given a string
S
S. Count the number of occurrences of all the digits in the string
S
S.

Input:
First line contains string
S
S.

Output:
For each digit starting from
0
0 to
9
9, print the count of their occurrences in the string
S
S. So, print
10
10 lines, each line containing
2
2 space separated integers. First integer
i
i and second integer count of occurrence of
i
i. See sample output for clarification.

Constraints:
 1
?
|
S
|
?
100
1?|S|?100

SAMPLE INPUT
77150
SAMPLE OUTPUT
0 1
1 1
2 0
3 0
4 0
5 1
6 0
7 2
8 0
9 0
'''

string = raw_input()
a0, b1, c2, d3, e4, f5, g6, h7, i8, j9 = 0,0,0,0,0,0,0,0,0,0
for i in string:
    if i == '0':
        a0 += 1
    elif i == '1':
        b1 += 1
    elif i == '2':
        c2 += 1
    elif i == '3':
        d3 += 1
    elif i == '4':
        e4 += 1
    elif i == '5':
        f5 += 1
    elif i == '6':
        g6 += 1
    elif i == '7':
        h7 += 1
    elif i == '8':
        i8 += 1
    elif i == '9':
        j9 += 1

print "0 "+ str(a0)
print "1 "+ str(b1)
print "2 "+ str(c2)
print "3 "+ str(d3)
print "4 "+ str(e4)
print "5 "+ str(f5)
print "6 "+ str(g6)
print "7 "+ str(h7)
print "8 "+ str(i8)
print "9 "+ str(j9)
