__author__ = 'Hinshitsu-IT'
'''
2000 and was not However, implemented 1998 it until;9 8 3 4 1 5 7 2
programming first The language;3 2 1
programs Manchester The written ran Mark 1952 1 in Autocode from;6 2 1 7 5 3 11 4 8 9

However, it was not implemented until 1998 and 2000
The first programming language
The Manchester Mark 1 ran programs written in Autocode from 1952
'''
test_cases = open('data_recovery.txt','r')
for test in test_cases:
    string , numbers = test.split(';')
    words = string.split()
    numbers = [int(i) for i in numbers.split()]
    maximum_range = len(words)

    for num in range(1,maximum_range+1):
        if num not in numbers:
            numbers.append(num)

    result = dict(zip(numbers, words))
    print(' '.join(result.values()))

