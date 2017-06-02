__author__ = 'narendra'

'''

https://www.hackerrank.com/contests/w32/challenges/duplication

Consider a binary string, , with an initial value of . We expand  by performing the following steps:

Create a string, , where each character  is equal to . For example, if , then . Note that  and  always have the same length because  is the complement of .
Append  to the end of  so that . In the example above,  becomes .
We keep on expanding  using steps  and  until the length of  exceeds .
When we repeat the expansion operation, string  grows like this:

Given  queries in the form of a zero-based index, , solve each query by printing the character at index  in  on a new line.

Input Format

The first line contains an integer denoting  (number of queries).
Each of the  subsequent lines contains an integer describing the value of  for a query.

Constraints

Output Format

For each query, print the value of  (i.e., either  or ) on a new line.

Sample Input 0

3
2
5
7
Sample Output 0

1
0
1
Explanation 0

First, we build string . Next, we answer the following sequence of  queries:

For ,  so we print  on a new line.
For ,  so we print  on a new line.
For ,  so we print  on a new line.
'''

#!/bin/python

import sys

# def duplication(x):
#     # Complete this function
#     s_initial = '0'
#     t_s_initial = '1'
#     flag = True
#     while flag:
#         s_expanded = s_initial + t_s_initial
#         s_initial = s_expanded
#         t_s_initial = s_expanded.replace("1", "2").replace("0", "1").replace("2", "0")
#         if len(s_expanded) > 1000:
#             flag = False
#     print s_expanded
#
# duplication(4)


def duplication(x):
    string = '0110100110010110100101100110100110010110011010010110100110010110100101100110100101101001100101100110100110010110100101100110100110010110011010010110100110010110011010011001011010010110011010010110100110010110100101100110100110010110011010010110100110010110100101100110100101101001100101100110100110010110100101100110100101101001100101101001011001101001100101100110100101101001100101100110100110010110100101100110100110010110011010010110100110010110100101100110100101101001100101100110100110010110100101100110100110010110011010010110100110010110011010011001011010010110011010010110100110010110100101100110100110010110011010010110100110010110011010011001011010010110011010011001011001101001011010011001011010010110011010010110100110010110011010011001011010010110011010010110100110010110100101100110100110010110011010010110100110010110100101100110100101101001100101100110100110010110100101100110100110010110011010010110100110010110011010011001011010010110011010010110100110010110100101100110100110010110011010010110100110010110'
    return string[x]

q = int(raw_input().strip())
for a0 in xrange(q):
    x = int(raw_input().strip())
    result = duplication(x)
    print(result)