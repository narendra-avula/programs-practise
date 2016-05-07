__author__ = 'Hinshitsu-IT'
'''
4 1 4 2 3
3 7 7 8
9 8 9 7 10 6 12 17 24 38

Jolly
Not jolly
Not jolly
'''

test_cases = open('jolly_jumpers.txt','r')

def difference(seq):
    diff = []
    for i in range(len(seq)-1):
        diff.append(abs(numbers[i]-numbers[i+1]))
    return diff


for test in test_cases:
    line = [int(i) for i in test.strip().split()]
    num_test = line[0]
    numbers = line[1:]
    print(difference(numbers))