__author__ = 'Hinshitsu IT'

def sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum

n = int(input())
s = input()
list=map(int,s.split(' '))
print (sum(list))