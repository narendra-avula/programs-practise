__author__ = 'Naidu'
'''
Golu wants to find out the sum of Lucky numbers.Lucky numbers are those numbers which contain exactly two set bits.This task is very diffcult for him.So Help Golu to find sum of those numbers which exactly contain two set bits upto a given number N.

3 5 10 are lucky numbers where 7 14 are not.

INPUT

First line contain number of test cases T.Each test case contains a single number N.
OUTPUT

Print sum of all Lucky Numbers upto N.Output may be large so take modulo with 1000000007.

Constraints

1<=T<=105
1<=N<=1018

NOTE: Since value of test cases and n is really large, please use fast I/O optimization techniques.

SAMPLE INPUT
1
5

SAMPLE OUTPUT
8

10
74173
6298825836169
254237658046
18611731882504
7044762251341
3888409234576
1512558478198
25306015973998
19602191892274
14643188793556

1916912
834626172
482485701
943085510
904346649
905692990
662176199
82189872
640626858
994614604
'''

def count_set_bits(number):
    count = 0
    while (number):
        number = number & (number-1)
        count += 1
    return count

def infinite_numbergenerator():
    n = 0
    while True:
         yield n
         n += 1

test_cases = int(raw_input())
while test_cases > 0:
    number = int(raw_input())
    sum = 0
    for i in range(number+1):
        if count_set_bits(i) == 2:
            sum += i
    print sum
    test_cases -= 1
