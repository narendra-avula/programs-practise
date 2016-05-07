__author__ = 'Hinshitsu-IT'
'''
6
2 3 10 12 15 22

2 10 12 22 46 3 15 18
'''
even = []
odd = []
input()
numbers = [int(x) for x in input().split()]
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

# print(even)
# print(odd)
print(' '.join([str(x) for x in sorted(even)]) + ' '+ str(sum(even))+' '+' '.join([str(y) for y in sorted(odd)]) + ' '+ str(sum(odd)))