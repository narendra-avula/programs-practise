__author__ = 'Hinshitsu-IT'
'''
1
7
22

1
1
0
'''

test_cases = open('happy_numbers.txt','r')
for test in test_cases:
    number = int(test.strip())

    visited = set()
    while 1:
        if number == 1:
            print ("1")
            break
        number = sum(int(c) ** 2 for c in str(number))
        print(number)
        if number in visited:
            print ("0")
            break
        visited.add(number)
        print(visited)
