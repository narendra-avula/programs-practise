__author__ = 'Hinshitsu IT'

def plus_minus(list):
    plus = 0
    minus = 0
    zero = 0
    for number in list:
        if number > 0:
            plus += 1
        elif number < 0:
            minus += 1
        elif number == 0:
            zero += 1
    cal_per(plus, minus, zero)

def cal_per(plus, minus, zero):
    print("{:.3f}".format(plus/n))
    print("{:.3f}".format(minus/n))
    print("{:.3f}".format(zero/n))

n = int(input())
s = input()
list=map(int,s.split(' '))
plus_minus(list)