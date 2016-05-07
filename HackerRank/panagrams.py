__author__ = 'Hinshitsu-IT'
'''
2
We promptly judged antique ivory buckles for the next prize
We promptly judged antique ivory buckles for the prize

'''

for _ in range(int(input())):
    string = list(set(input()))
    if (len(string)) > 26:
        print('pangram')
    else:
        print('not pangram')