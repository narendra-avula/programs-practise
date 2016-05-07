__author__ = 'Hinshitsu-IT'
'''
10
1
2
3
4
5
6
7
8
9
10

3
'''
# n = []
# for _ in range(int(input())):
#     n.append (int(input()))
# count = 0
# for i in n:
#     if i % 3 == 0:
#         count += 1
# print(count)

print(len([a for a in range (input()) if input()%3==0]))
