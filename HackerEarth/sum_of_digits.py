__author__ = 'Hinshitsu-IT'
'''
3
1
2
3

0

'''
def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n /= 10
    return sum

numbers = []
test_cases = int(input())
if test_cases >= 2 and test_cases <= 10000:
    for _ in range():
        numbers.append(int(input()))
    # print(numbers)

digit_sum = 0
for number in numbers:
    digit_sum += sum_digits(number)

print((int(digit_sum))%9 - (sum(numbers)%9))
