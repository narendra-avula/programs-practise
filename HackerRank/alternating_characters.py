__author__ = 'Hinshitsu-IT'
'''
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB

3
4
0
0
4
'''

for _ in range(int(input())):
    string  = input()
    count = 0
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
    print(count)