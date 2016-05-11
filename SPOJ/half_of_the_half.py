__author__ = 'CustomFurnish'

'''
Input:
4
your
progress
is
noticeable

Output:

y
po
i
ntc

'''

for _ in range(int(input())):
    string = input()
    length = int(len(string))/2
    # print(length)
    # for i in range(0,int(length),2):
    #     print(string[i])
    print(''.join(string[j] for j in range(0,int(length),2)))