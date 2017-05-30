__author__ = 'narendra'

numbers_length = int(raw_input())
numbers = map(int, raw_input().split())

numbers.sort()
total = sum(numbers)

for num in numbers:
    if num * len(numbers) > total:
        print num
        break
