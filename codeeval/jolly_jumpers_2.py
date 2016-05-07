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

for test in test_cases:
    numbers = [int(i) for i in test.split()[1:]]
    positions = [i for i in range(1, len(numbers))]
    diffs = sorted(map((lambda x, y: abs(x -y)), numbers[:-1], numbers[1:]))
    print ('Jolly' if diffs == positions else 'Not jolly')