__author__ = 'narendra'

'''
Julius Cipher is a type of cipher which relates all the lowercase alphabets to their numerical position in the alphabet, i.e., value of a is 1, value of b is 2, value of z is 26 and similarly for the rest of them.

Little Chandan is obsessed with this Cipher and he keeps converting every single string he gets, to the final value one gets after the multiplication of the Julius Cipher values of a string. Arjit is fed up of Chandan's silly activities, so he decides to at least restrict Chandan's bad habits.

So, he asks Chandan not to touch any string which is a palindrome, otherwise he is allowed to find the product of the Julius Cipher values of the string.

Input:
The first line contains t number of test cases. The first line of every test case contains a string, S.

Output:
Print the value if the string is not a palindrome, otherwise print Palindrome - where value is equal to the product of all the characters of Julius Cipher values.

Constraints: 1 <= T <= 102
1<=length of the string<=10

Note:
The string will contain only lowercase letters.

SAMPLE INPUT
2
zazaz
goodarjit
SAMPLE OUTPUT
Palindrome
204120000
'''

def isprime(number):
    if number == 2:
        return True
    if number == 3:
        return True
    if number % 2 == 0:
        return False
    if number % 3 == 0:
        return False

    start = 5
    interval = 2

    while start * start <= number:
        if number % start == 0:
            return False

        start += interval
        interval = 6 - interval

    return True

def is_prime_string(string):
    if string == string[::-1]:
        return True
    else:
        return False

def product_string(string):
    product = 1
    for i in range(len(string)):
        product *= ord(string[i]) - 96
    return product

test_cases = int(raw_input())
for _ in range(test_cases):
    string = raw_input()
    string_length = len(string)
    if is_prime_string(string):
        print "Palindrome"
    else:
        print product_string(string)