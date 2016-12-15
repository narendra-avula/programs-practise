__author__ = 'narendra'


def squares(number):
    perfect_squares =  [x*x for x in range(1,number) ]
    return [num for num in perfect_squares if num < number]

for _ in range(int(input())):
    number = int(input())
    print len(squares(number))