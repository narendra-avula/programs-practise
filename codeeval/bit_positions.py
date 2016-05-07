__author__ = 'Hinshitsu-IT'
'''
86,2,3
125,1,2

true
false
'''

test_cases = open('bit_positions.txt','r')
for test in test_cases:
    number, pos_1, pos_2 = map(int, test.strip().split(','))
    # print(number, pos_1, pos_2)
    bin_number = bin(number)
    if bin_number[-pos_1] == bin_number[-pos_2]:
        print('true')
    else:
        print('false')
