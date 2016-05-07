__author__ = 'Hinshitsu-IT'

def sum_digits(n):
    sum = 0
    while n:
        sum = sum + (n % 10)
        print(sum)
        n = n // 10
        print(n)
    return sum

print(sum_digits(12345))

# input_list = ['1', '2', '3', '4', '5', '12',
#               '13', '14', '15', '23', '24', '25', '34', '35',
#               '45', '123', '124', '125', '134', '135', '145', '234',
#               '235', '245', '345', '1234', '1235', '1245', '1345', '2345', '12345']
#
# sum = 0
# sum_total = []
# input_list = [int(i) for i in input_list]
# print(input_list)
#
# for i in input_list:
#     sum += sum_digits(i)
#     sum_total.append(sum_digits(i))
# print(sum_total)
# print(sum)