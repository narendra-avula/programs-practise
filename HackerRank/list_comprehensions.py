__author__ = 'Hinshitsu-IT'
'''
1
1
1
2

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
'''

a = int(input())+1
b = int(input())+1
c = int(input())+1
d = int(input())
print ([[x,y,z] for x in range(a) for y in range(b) for z in range(c) if sum([x,y,z])!=d])