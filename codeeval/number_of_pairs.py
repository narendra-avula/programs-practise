__author__ = 'Hinshitsu-IT'
"""
Number Pairs.
Challenge Description:
You are given a sorted array of positive integers and a number 'X'. Print out
all pairs of numbers whose sum is equal to X. Print out only unique pairs and
the pairs should be in ascending order
Input sample:
Your program should accept as its first argument a filename. This file will
contain a comma separated list of sorted numbers and then the sum 'X',
separated by semicolon. Ignore all empty lines. If no pair exists, print the
string NULL e.g.
1,2,3,4,6;5
2,4,5,6,9,11,15;20
1,2,3,4;50
Output sample:
Print out the pairs of numbers that equal to the sum X. The pairs should
themselves be printed in sorted order i.e the first number of each pair should
be in ascending order. E.g.
1,4;2,3
5,15;9,11
NULL

1,2,3,4,6;5
2,4,5,6,9,11,15;20
1,2,3,4;50

1,4;2,3
5,15;9,11
NULL

"""
from  itertools import combinations
test_cases = open('number_of_pairs.txt','r')
for test in test_cases:
    numbers , sum_total = test.strip().split(';')
    numbers = [int(i) for i in numbers.split(',')]
    result = []
    for i in combinations(numbers,2):
        if sum(i) == int(sum_total):
            result.append(','.join(str(l) for l in i))
    if result:
        print(';'.join(result))
    else:
        print('NULL')

    # text, num = (int(i) for i in
    #              test.split(';')[0].split(',')), int(test.split(';')[1])
    # out = [','.join(str(l) for l in i) for i in
    #        list(itertools.combinations(text, 2)) if sum(i) == num]
    # print (';'.join(out) if out else 'NULL')