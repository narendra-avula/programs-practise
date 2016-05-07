__author__ = 'Hinshitsu-IT'
'''
92,19,19,76,19,21,19,85,19,19,19,94,19,19,22,67,83,19,19,54,59,1,19,19
92,11,30,92,1,11,92,38,92,92,43,92,92,51,92,36,97,92,92,92,43,22,84,92,92
4,79,89,98,48,42,39,79,55,70,21,39,98,16,96,2,10,24,14,47,0,50,95,20,95,48,50,12,42

19
92
None
'''
import operator
test_cases = open('major_element.txt','r')
for test in test_cases:
    numbers = list(map(int, test.strip().split(',')))
    # print(len(numbers))
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    # print(counts)

    max_number = None
    max_count = None
    for n , c in counts.items():
        if max_count is None or c > max_count:
            max_count = c
            max_number = n
    # print(max_number, max_count)

    if len(numbers)/2 < max_count:
        print(max_number)
    else:
        print('None')
