__author__ = 'Hinshitsu IT'

percentage = dict()
for i in range(int(input())):
    a = input().split()
    name = a[0]
    numbers = [float(x) for x in a[1:]]
    per = sum(numbers)/len(numbers)
    percentage[name] = '%.2f'%per


name = input()
print(percentage[name])