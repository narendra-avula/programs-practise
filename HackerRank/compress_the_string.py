__author__ = 'narendra'

'''
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string .

Output Format

A single line of output consisting of the modified string.

Constraints

All the characters of  denote integers between  and .


Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
Explanation

First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced by  and so on.

Also, note the single space within each compression and between the compressions.
'''



# input_string = raw_input()
# print (*[(len(list(c)), int(k)) for k, c in groupby(input())])

# from itertools import groupby
# input_string = raw_input()
# compress_string = []
# for k, c in groupby(input_string):
#     compress_string.append( (len(list(c)), int(k)) )
# print " ".join(str(x) for x in compress_string)

string = raw_input()
current = string[0]
count = 0
for i in xrange(len(string)):
    if string[i] == current:
        count += 1
    else:
        print "(%d, %s)" % (count, current),
        current = string[i]
        count = 1
print "(%d, %s)" % (count, current)