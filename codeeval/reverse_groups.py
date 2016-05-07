__author__ = 'Hinshitsu-IT'
'''
1,2,3,4,5;2
1,2,3,4,5;3

2,1,4,3,5
3,2,1,4,5
'''

test_cases = open('reverse_groups.txt','r')
for test in test_cases:
    numbers, chunk = test.split(';')
    numbers = [int(i) for i in numbers.split(',')]
    chunk = int(chunk)
    # print(numbers)
    # print(chunk)
    result = [','.join(str(i) for i in numbers[i:i+chunk][::-1]) for i in range(0, len(numbers), chunk)]
    print(','.join(result))




# l = [1,2,3,4,5]
# chunk = 2
# print(','.join(','.join(str(i) for i in l[i:i+2][::-1]) for i in range(0, len(l), 2)))