__author__ = 'Hinshitsu-IT'
'''
1
4
2
1
4
3

1 0 1 0
'''

for _ in range(int(input())):
    numbers = []
    for i in range(int(input())):
        numbers.append(int(input()))
    # print(numbers)

    for i in numbers:
        num = i
        num_index = numbers.index(i)
        # print(i, num_index)
        count = 0
        for j in range(num_index,len(numbers)):
            if numbers[j] < num:
                count += 1
        print(count)


