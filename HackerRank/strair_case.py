__author__ = 'Hinshitsu IT'

stairs = int(input())
for i in range(1, stairs + 1):
    print (' ' * (stairs - i) + '#' * i)

