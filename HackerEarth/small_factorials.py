__author__ = 'Hinshitsu-IT'

kases = int(input())
for kase in range(kases):
    N = int(input())
    result = 1
    for i in range(1, N + 1):
        result = result * i
    print (result)