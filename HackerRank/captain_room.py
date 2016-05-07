__author__ = 'Hinshitsu IT'


input()
digits = input().split()
counts = dict()
for num in digits:
    counts[num] = counts.get(num, 0) + 1

number = None
number_count = None
for num,count in counts.items():
    if number is None or count < number_count:
        number = num
        number_count = count

print(number)
