__author__ = 'Hinshitsu-IT'

'''
3
wyyga
qwertyuioplkjhgfdsazxcvbnm
ejuxggfsts

NO
YES
NO
'''

import sys
if sys.version_info[0]>=3:
    raw_input=input

from string import ascii_lowercase
lower_case = ascii_lowercase
lower_case = list(lower_case)
print(lower_case)
# print(len(lower_case))

for _ in range(int(input())):
    input_list = list(input())
    print(input_list)
    for i in input_list:
        if i in lower_case:
            print(i)
            input_list.remove(i)
            lower_case.remove(i)

    # print(len(input_list))
    # print(len(lower_case))

    if len(input_list) == len(lower_case):
        print('YES')
    else:
        print('NO')


