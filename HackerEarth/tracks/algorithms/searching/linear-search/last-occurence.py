__author__ = 'Naidu'
'''
You have been given an array of size
N
N consisting of integers. In addition you have been given an element
M
M you need to find and print the index of the last occurrence of this element
M
M in the array if it exists in it, otherwise print -1. Consider this array to be 1 indexed.

Input Format:

The first line consists of 2 integers
N
N and
M
M denoting the size of the array and the element to be searched for in the array respectively . The next line contains
N
N space separated integers denoting the elements of of the array.

Output Format

Print a single integer denoting the index of the last occurrence of integer
M
M in the array if it exists, otherwise print -1.

Constraints

1
?
N
?
10
5
1?N?105

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
1
?
M
?
10
9
1?M?109

SAMPLE INPUT
5 1
1 2 3 4 1

SAMPLE OUTPUT
5
'''

length, key = map(int, raw_input().split())
array = map(int, raw_input().split())
temp = 0
for i in range(length):
    if array[i] == key:
        temp = array.index(array[i],i)
if temp == 0:
    print -1
else:
    print temp + 1