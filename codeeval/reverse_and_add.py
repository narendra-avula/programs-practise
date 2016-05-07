__author__ = 'Hinshitsu-IT'
'''
195


'''
# import math
# def is_prime(n):
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True

def is_palindrome(n):
    if int(str(n)[::-1]) == int(n):
        return True
    else:
        return False

def reverse_num(n):
    rev = 0
    while(n > 0):
        rev = (10*rev)+n%10
        n //= 10
    return rev

fhand = open('reverse_and_add.txt','r')
for line in fhand:
    number = int(line)
    check_number = number + reverse_num(number)
    count = 1
    flag = True
    while(flag):
        if is_palindrome(check_number):
            print(count, check_number)
            flag = False
        else:
            check_number = check_number + reverse_num(check_number)
            count += 1
