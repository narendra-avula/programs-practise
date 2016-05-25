__author__ = 'Naidu'
'''
You have been given an array
A
A of size
N
N consisting of positive integers. You need to find and print the product of all the number in this array Modulo
10
9
+
7
109+7.

Input Format:
The first line contains a single integer
N
N denoting the size of the array. The next line contains
N
N space separated integers denoting the elements of the array

Output Format:
Print a single integer denoting the product of all the elements of the array Modulo
10
9
+
7
109+7.

Constraints:
1
?
N
?
10
3
1?N?103
1
?
A
[
i
]
?
10
3
1?A[i]?103

SAMPLE INPUT
5
1 2 3 4 5
SAMPLE OUTPUT
120
'''

N = int(raw_input())
A = map(int, raw_input().split())
answer = 1
for i in A:
    answer = (answer * i) % (10**9 + 7)
print answer

