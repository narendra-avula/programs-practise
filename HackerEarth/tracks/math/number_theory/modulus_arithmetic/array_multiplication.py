__author__ = 'Naidu'
'''
You have been given an array of integers
A
A of size
N
N. You need to find the product of all the numbers in the array modulo
10
9
+
7
109+7.

Input Format:

The First line contains a single integer
N
N denoting the size of the array. The next line contains
N
N space separated integers denoting the elements of array
A
A.

Output Format:

Print a single integer denoting the product of all numbers in array
A
A modulo
10
9
+
7
109+7

Constraints:

1
?
N
?
10
4
1?N?104
1
?
A
[
i
]
?
10
9
1?A[i]?109

SAMPLE INPUT
5

1 1 1 1 1
SAMPLE OUTPUT
1
'''

n = int(raw_input())
a = map(int, raw_input().split())
prod = 1
for i in a:
    prod *= i
print prod % (10 ** 9 + 7)