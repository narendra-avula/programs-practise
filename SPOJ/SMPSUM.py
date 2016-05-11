__author__ = 'CustomFurnish'
'''
Input:
1 4

Output:
30
Example 2

Input:
5 6

Output:
61

'''

# start, end = map(int, input().split())
# sum = 0
# for i in range(start, end+1):
#     sum = sum + i * i
# print(sum)
start, end = map(int, input().split())
print(sum(i * i for i in range(start, end+1) ))
