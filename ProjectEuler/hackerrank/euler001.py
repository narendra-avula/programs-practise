__author__ = 'narendra'

'''
Project Euler #1: Multiples of 3 and 5

If we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .

Find the sum of all the multiples of  or  below .

Input Format

First line contains  that denotes the number of test cases. This is followed by  lines, each containing an integer, .

Constraints

Output Format

For each test case, print an integer that denotes the sum of all the multiples of  or  below .

Sample Input 0

2
10
100
Sample Output 0

23
2318
Explanation 0

For , if we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .

Similarly for , we get .
'''



# def sum_n(n, d) :
#     n = int(n/d)
#     return int(d * n * (n + 1) / 2)
#
#
# test_cases = int(raw_input().strip())
# for test in range(test_cases):
#     number = int(raw_input().strip())
#     print (sum_n(number, 3) + sum_n(number, 5) - sum_n(number, 15))




# def sum_of_numbers(numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total
#
# def get_mul_three_five(number):
#     mul_numbers = []
#     for i in range(number):
#         if ( int(i % 3) == 0 ) or ( int(i % 5) == 0 ):
#             mul_numbers.append(i)
#     return mul_numbers

# test_cases = int(raw_input().strip())
# for test in range(test_cases):
#     number = int(raw_input().strip())
#     numbers = get_mul_three_five(number)
#     print sum_of_numbers(numbers)



class E:
    def __init__(self, x):
        self.num = x
        self.a = self.sumOfNumber(3)
        self.b = self.sumOfNumber(5)
        self.c = self.sumOfNumber(15)
        print self.a+self.b-self.c

    def sumOfNumber(self, num):
        a = num
        d = num
        l = self.lastNumber(num)
        n = ((l-a)/d)+1
        return (n*(a+l))/2

    def lastNumber(self, num):
        i = 0
        for a in xrange(self.num):
            if a%num == 0:
                i = a
        return i

if __name__ == '__main__':
    cases = int(raw_input())
    for i in xrange(cases):
        E(int(raw_input()))