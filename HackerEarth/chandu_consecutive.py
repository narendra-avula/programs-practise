__author__ = 'Hinshitsu-IT'

'''
3
abb
aaab
ababa

ab
ab
ababa
'''
for _ in range(int(input())):
    input_list = list(input())
    # print(input_list)
    new_list = []
    for i in range(len(input_list)-1):
        if input_list[i] != input_list[i+1]:
            new_list.append(input_list[i])
    new_list.append(input_list[-1])
    print(''.join(new_list))

