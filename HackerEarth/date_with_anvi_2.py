__author__ = 'Hinshitsu-IT'
'''
3
1
2
3

1
12 21
123 132 213 231 312 321
'''
from itertools import permutations

# print([list(combinations(['a','b','c'],i)) for i in range(1,4)])

for _ in range(int(input())):
    numbers = []
    n = int(input())
    print (" ".join([str("".join(map(str,i))) for i in permutations(range(1,n+1),n)]))
    # for i in range(1,n+1):
    #     numbers.append(str(i))
    # # print(''.join(numbers))
    #
    # for e in permutations(sorted(numbers),len(numbers)):
    #     print(''.join(e))



