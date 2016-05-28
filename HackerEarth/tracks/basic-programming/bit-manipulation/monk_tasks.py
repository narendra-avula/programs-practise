__author__ = 'Hinshitsu-IT'
'''
1
4
3 4 7 10

4 3 10 7
'''


# print(bin(7)[2:].count('1'))
from collections import defaultdict

for _ in range(int(input())):
    n = input()
    numbers = list(map(int,input().split()))
    num_dict = {}
    print(numbers)
    for i in numbers:
        num_dict[i] = (bin(i)[2:].count('1'))
    print(num_dict)
    num_dict_2 = defaultdict((y,x) for x,y in num_dict.items())
    print(num_dict_2)

    l = [num_dict_2[key] for (key, value) in sorted(num_dict_2.items(), reverse=False)]
    print(l)