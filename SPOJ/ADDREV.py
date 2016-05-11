__author__ = 'CustomFurnish'
'''
Sample input:

3
24 1
4358 754
305 794

Sample output:

34
1998
1

'''

def reverse(num):
  rev = 0
  while(num > 0):
    rev = (10*rev)+num%10
    num //= 10
  return rev

# print(reverse(1000))

for _ in range(int(input())):
    num_1, num_2 = map(int, input().split())
    result = reverse(reverse(num_1) + reverse(num_2))
    print(result)