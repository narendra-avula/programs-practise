__author__ = 'Hinshitsu-IT'
'''
1 2 3 4 5 6 7 8 9 : 0-8
1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3

9 2 3 4 5 6 7 8 1
2 4 3 1 5 6 7 8 9 10
'''
fhand = open('swap_elements.txt','r')
for line in fhand:
    numbers, swap_range = line.strip().split(':')
    numbers = numbers.split()
    swap_range_list = swap_range.strip().split(',')
    for r in swap_range_list:
        start, end = r.split('-')
        start , end = int(start), int(end)
        a, b = numbers[start],numbers[end]
        numbers[start] , numbers[end] = b, a
    print(' '.join(str(i) for i in numbers))