__author__ = 'Hinshitsu-IT'

'''
2
remember
occurring

KISS
SLAP

'''
for _ in range(int(input())):
    input_list = list(input())
    count = 0
    for i in range(len(input_list)-1):
        if input_list[i] == input_list[i+1]:
            count += 1

    if count == 0:
        print('KISS')
    else:
        print('SLAP')
