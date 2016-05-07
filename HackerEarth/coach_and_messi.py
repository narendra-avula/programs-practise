__author__ = 'Hinshitsu-IT'
'''
3
2 2
3 4
250000000 4

4
81
660156264
'''
# x = 1000000007
# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     if a ** b < x:
#         print(a**b)
#     else:
#         print((a**b)%x)

for i in range(int(input())):
    a,b=map(int,input().split())
    print(pow(a,b,1000000007))
