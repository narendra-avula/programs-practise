__author__ = 'narendra'
'''
HackerMan has brought a new drawing book for his child, which consists only of geometric shapes. Its consists of lessons where the child has to make drawings using the geometric shapes. The first lesson is based on how to use squares to build different objects.

You are task is to help HackerMan in teaching one part of this lesson. You have to help him in determining, given S number of squares, how many distinct rectangles you can build out of that.

Two rectangles are considered different if none of them can be rotated and moved to obtain the second one. During rectangle construction, the child can neither deform the squares nor put any squares upon any other ones.

Note: All the squares are of the same configuration.

Constraints

Each file will not contain T test cases where

Input

There will be one line of input that will contain an integer
S
S that represents the number of squares available.

Output

Each line should contain a single integer equal to the number of different rectangles that the child can form using the corresponding number of squares in that line of input.

Explanation of sample below

There are a total of
3
3 test cases.

Only
1
1 rectangle can be made using
1
1 square, and its the square itself.

2
2 rectangles can be made using
2
2 square, one is the square itself and the other is formed by joining the
2
2 squares.

A total of
5
5 rectangles can be made using
4
4 squares.
4
4 rectangles will be only
1
1 square wide and
1
1 rectangle will be
2
2 squares wide.

SAMPLE INPUT
3
1
2
4
SAMPLE OUTPUT
1
2
5
'''

# test_cases = int(raw_input())
# for _ in range(test_cases):
#     number = int(raw_input())
#     if number == 1:
#         print "1"
#     else:
#         print ( (3 * number ) / 2) - 1

test_cases = int(raw_input())
for _ in range(test_cases):
    rectangles = 0
    squares = int(raw_input())
    for i in range(1, int(squares ** 0.5) + 1):
        rectangles += int (squares/i) - (i-1)
    print rectangles