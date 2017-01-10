__author__ = 'Narendra'

'''
3
wyyga
qwertyuioplkjhgfdsazxcvbnm
ejuxggfsts

NO
YES
NO
'''

for i in range(int(input())):
    input_list = list(set(input().strip()))
    if len(input_list) >= 26:
        print('YES')
    else:
        print('NO')