__author__ = 'Naidu'
'''
After the Tatvik Hiring Challenge, Karan's NLP professor has given him another homework. Since Manhattan Associates Hiring Challenge is round the corner and Karan is busy preparing for it, he turns to you for help.

Given a string, replace all the consecutively occurring characters by a single, same character.

Input:

The first line contains the number of test cases T. Each test case contains the string, on a separate line.

Output:

Print the modified string, each on a new line.

Constraints:

1 <= T <= 100

1 <= length(string) < 10^6

SAMPLE INPUT
1
aabbcc

SAMPLE OUTPUT
abc
'''
from itertools import groupby
ans=[]
def remove_duplicates(arg):
    unique = (i[0] for i in groupby(arg))
    return ''.join(unique)

for i in range(int(raw_input())):
		ans.append(remove_duplicates(raw_input()))

for res in ans:
	print (res)