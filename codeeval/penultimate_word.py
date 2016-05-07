__author__ = 'Hinshitsu-IT'
'''
some line with text
another line

with
another
'''

test_cases = open('penultimate_word.txt','r')
for test in test_cases:
    print(test.strip().split()[-2])