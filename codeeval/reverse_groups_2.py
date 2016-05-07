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
    last = (len(numbers) - (len(numbers) % chunk)) - 1
    if chunk != 1:
        for i in range(0, last, chunk):
            numbers[i:i + chunk] = numbers[i:i + chunk][::-1]

    print (','.join(str(i) for i in numbers))



