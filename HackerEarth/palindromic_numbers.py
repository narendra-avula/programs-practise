__author__ = 'Hinshitsu-IT'

'''
2
10 13
20 30

1
1

'''

# def reverse(num):
#   rev = 0
#   while(num > 0):
#     rev = (10*rev)+ num%10
#     num //= 10
#   return rev

def reverse(num):
  return int(str(num)[::-1])
for _ in range(int(input())):
    start, last = map(int, input().split())
    count = 0
    for i in range(start, last+1):
        if i == reverse(i):
            count += 1
    print(count)