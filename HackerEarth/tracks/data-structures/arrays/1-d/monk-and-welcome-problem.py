__author__ = 'narendra'
'''
Having a good previous year, Monk is back to teach algorithms and data structures.

This year he welcomes the learners with a problem which he calls "Welcome Problem". The problem gives you two arrays
A
A and
B
B (each array of size
N
N) and asks to print new array
C
C such that:

Now, Monk will proceed further when you solve this one. So, go on and solve it :)

Input:
First line consists of an integer
N
N, denoting the size of
A
A and
B
B.
Next line consists of
N
N space separated integers denoting the array
A
A.
Next line consists of
N
N space separated integers denoting the array
B
B.

Output:
Print
N
N space separated integers denoting the array
C
C.


SAMPLE INPUT
5
1 2 3 4 5
4 5 3 2 10
SAMPLE OUTPUT
5 7 6 6 15
'''

array_size = int(raw_input())
array_a = map(int, raw_input().split())
array_b = map(int, raw_input().split())
array_c = []
for i in range(array_size):
    array_c.append(array_a[i] + array_b[i])
print ' '.join(str(j) for j in array_c)


n=input()
a=map(int,raw_input().split())
b=map(int,raw_input().split())
for i in range(n):
    print a[i]+b[i],