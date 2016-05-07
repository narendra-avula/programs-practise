__author__ = 'Hinshitsu-IT'
'''
a b c d 4
e f g h 2

a
g
'''

test_cases = open('mth_last_element.txt','r')
for test in test_cases:
    # test = test.strip().split()
    # letters = test[:-1]
    # number = int(test[-1])
    # if len(letters) < number:
    #     print()
    # else:
    #     print(letters[-number])

    # test = list(reversed(test.strip().split(' ')))
    # print(test[int(test[0])])

    elements = test.strip().split()
    index_last = int(elements[-1]) + 1
    if index_last > len(elements):
        pass
    else:
        print (elements[-index_last])
