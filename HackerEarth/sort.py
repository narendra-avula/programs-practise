__author__ = 'Hinshitsu-IT'
'''
8
567
23
-10982
1000000
-999999
-3456
1729
65535

-999999
-10982
-3456
23
567
1729
65535
1000000
'''
numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
# plus = []
# minus = []
# zero = []
# for number in numbers:
#     if number > 0:
#         plus.append(number)
#     elif number < 0:
#         minus.append(number)
#     else:
#         zero.append(number)
#
# print('\n'.join(str(i) for i in sorted(minus,reverse=False)))
# print('\n'.join(str(i) for i in sorted(plus,reverse=False)))
print('\n'.join(str(i) for i in sorted(numbers)))