__author__ = 'Hinshitsu IT'

number = int(input())
for i in range(number):
    lists = [int(i) for i in input().split()]
#print(lists)
    x = 2 * lists[2] - lists[0]
    y = 2 * lists[3] - lists[1]
    print(str(x) +" "+str(y) )