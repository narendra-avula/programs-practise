__author__ = 'CustomFurnish'

'''
All submissions for this problem are available.

For help on this problem, please check out our bit-manipulation-tutorial Input and Output (I/O)

Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything. More precisely... rewrite small numbers from input to output. Stop processing input after reading in the number 42. All numbers at input are integers of one or two digits.
Example


Input:
1
2
88
42
99

Output:
1
2
88
'''

while(True):
    number = int(input())
    if number == 42:
        break
    print(number)