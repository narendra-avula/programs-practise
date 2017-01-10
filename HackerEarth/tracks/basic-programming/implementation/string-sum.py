__author__ = 'narendra'
'''
Consider All lowercase Alphabets of the English language. Here we consider each alphabet from
a
a to
z
z to have a certain weight. The weight of the alphabet
a
a is considered to be
1
1,
b
b to be
2
2,
c
c to be
3
3 and so on until
z
z has a weight of
26
26. In short, the weight of the alphabet
a
a is
1
1, and the weight of all other alphabets is the weight of its previous alphabet +
1
1.

Now, you have been given a String
S
S consisting of lowercase English characters. You need to find the summation of weight of each character in this String.

For example, Consider the String
a
b
a
aba
Here, the first character
a
a has a weight of
1
1, the second character
b
b has
2
2 and the third character
a
a again has a weight of
1
1. So the summation here is equal to :
1
+
2
+
1
=
4
1+2+1=4

Input Format:
The first and only line of input contains the String
S
S.

Output Format
Print the required answer on a single line

Constraints
 1
|
S
|

1000

SAMPLE INPUT
aba
SAMPLE OUTPUT
4

Explanation
Explanation for the Sample has been given in the Problem Statement.
'''

from string import lowercase

def get_lowercase():
    lowercase_dict = {}
    for i in range(1, 27):
        lowercase_dict[lowercase[i - 1]] = (i)
    return lowercase_dict

def main():
    string = raw_input()
    string_sum = 0
    lowercase_dict = get_lowercase()
    for i in string:
        string_sum += lowercase_dict[i]
    print string_sum

def main_2():
    string = raw_input()
    total = 0
    for i in range(len(string)):
        total += ord(string[i]) - 96
    print total

def main_3():
    string = lowercase
    total = 0
    for i in range(len(string)):
        total += ord(string[i]) - 96
    print total

if __name__ == '__main__':
    # main()
    # main_2()
    main_3()
