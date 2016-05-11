__author__ = 'CustomFurnish'
'''
All submissions for this problem are available.

Given the list of numbers, you are to sort them in non decreasing order.
Input


Output

Output given numbers in non decreasing order.
Example

Input:
5
5
3
6
7
1

Output:
1
3
5
6
7

'''

# a = [input() for _ in range(int(input()))]
# a.sort()
# for i in a:
#     print(i)

# inp = raw_input()
# n = int(inp)
# A = list()
# counter = n
# while counter > 0 :
#     A.append(int(raw_input()))
#     counter-=1
# A.sort()
# for i in range(n) :
#     print A[i]

n = int(input())
counter = n
a = list()
while counter > 0:
    a.append(int(input()))
    counter -= 1
a.sort()
for i in a:
    print(i)