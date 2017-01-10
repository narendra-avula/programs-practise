__author__ = 'Naidu'
'''
Given a string
S
S made of English alphabets, find the count of all the vowels in
S
S. Vowels are
[
a
,
e
,
i
,
o
,
u
]
[a,e,i,o,u]. Task is to print the count of all those vowels occurring in the string
S
S.
Approach:

There are five vowels in English alphabet. Declare a space for five integers, initialize them as
0
0.
Traverse the string
S
S, character by character, check if the character is vowel. If it is, increment the count of that vowel.
Print out the count of each vowel after the iteration over the string is done.
'''

string = raw_input()
a , e, i, o, u = 0, 0, 0, 0, 0
for char in string:
    if char == 'a':
        a += 1
    elif char == 'e':
        e += 1
    elif char == 'i':
        i += 1
    elif char == 'o':
        o += 1
    elif char == 'u':
        u += 1

print "a= "+ str(a)
print "e= "+ str(e)
print "i= "+ str(i)
print "o= "+ str(o)
print "u= "+ str(u)