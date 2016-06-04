__author__ = 'Naidu'

'''
Print Array in Reverse
Given the size and the elements of array
A
A, print all the elements in reverse order.

Input:
First line of input contains,
N
N - size of the array.
Following N lines, each contains one integer,
i
t
h
ith element of the array i.e.
A
[
i
]
A[i].

Output:
Print all the elements of the array in reverse order, each element in a new line.

Constraints:

1
?
N
?
100
1?N?100
0
?
A
[
i
]
?
1000
0?A[i]?1000
SAMPLE INPUT
5
4
12
7
15
9
SAMPLE OUTPUT
9
15
7
12
4
'''


array_size = int(raw_input())
array = []
for i in range(array_size):
    array.append(int(raw_input()))

for i in array:
    print i

for i in array[::-1]:
    print i