__author__ = 'Hinshitsu-IT'
'''
3413289830 a-bcdefghij
776 a+bc
12345 a+bcde
1232 ab+cd
90602 a+bcde

-413289827
83
2346
44
611
'''
import re
test_cases = open('split_the_number.txt','r')
for test in test_cases:
    number, string = test.split()
    number = str(number)
    symbol = re.sub("[a-zA-Z]+", "",string)
    symbol_index = string.index(symbol)
    before = int(number[:symbol_index])
    after = int(number[symbol_index:])
    # print(before, after)
    print( eval(str(before)+symbol+str(after)) )






