__author__ = 'Hinshitsu IT'

input()
set_1 = set(map(int, input().split()))
input()
set_2 = set(map(int, input().split()))
list_1 = list(set_1.symmetric_difference(set_2))
list_1.sort()
for i in list_1:
    print(i)