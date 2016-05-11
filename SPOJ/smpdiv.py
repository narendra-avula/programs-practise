__author__ = 'CustomFurnish'

'''
Input:
2
7 2 4
35 5 12

Output:
2 6
5 10 15 20 25 30

'''

for _ in range(int(input())):
    end, start, drop = map(int, input().split())
    # print(start, end, drop)
    # list = [i for i in range(start,end,start) if i != drop]
    # print(list)

    if start < end:
        print(' '.join(str(j) for j in [i for i in range(start,end,start) if i != drop]))

    # for i in range(start,end,start):
    #     if i != drop:
    #         print(i, end=" ")
    # print('\n')
