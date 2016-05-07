__author__ = 'Hinshitsu-IT'
'''
Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output

200
'''

from collections import Counter
input()
sizes_list = [int(x) for x in input().split()]
# print(sizes_list)
# sizes_dict = Counter(sizes_list)
# print(sizes_dict)

sum = 0
for _ in range(int(input())):
    size, price = input().split()
    size, price = int(size),int(price)
    if size in sizes_list:
        sum += price
        sizes_list.remove(size)
print(sum)