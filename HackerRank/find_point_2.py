__author__ = 'Hinshitsu IT'
number = int(input())
for i in range(number):
        Px, Py, Qx, Qy = list(map(int, input().split()))
        print(2 * Qx - Px, 2 * Qy - Py)