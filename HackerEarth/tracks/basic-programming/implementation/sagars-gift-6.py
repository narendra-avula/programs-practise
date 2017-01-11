__author__ = 'narendra'

'''
Today is Sagar's birthday. He got array of numbers as a gift by his father. His father told him that he has another gift if Sagar is able make largest number by concatenating the numbers and swapping the digits of numbers. Help Sagar to make largest number from the given numbers.

Input:

First line contains number of testcases T Next line contain value of number of values in array N Followed by N space separated number

Output:

Output the answer.

Constraint :

1<= T <=10

1<= N <=100

1<= a[i] <= 10000

SAMPLE INPUT
2
5
1 2 20 31 5
4
9 1 5 10

SAMPLE OUTPUT
5322110
95110

'''
def get_digits(array):
    digits = []
    for num in array:
        digits += list(num)
    digits = [int(i) for i in digits]
    digits.sort(reverse=True)
    print ''.join(str(i) for i in digits)

if __name__ == '__main__':
    testcases = int(raw_input())
    for _ in range(testcases):
        array_size = int(raw_input())
        array = raw_input().split()
        digits = get_digits(array)