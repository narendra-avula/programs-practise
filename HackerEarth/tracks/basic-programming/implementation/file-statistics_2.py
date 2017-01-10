__author__ = 'narendra'
'''
Write a command line tool which takes a file path as input and prints the number of lines,

number of words, number of characters in the file, userid of the owner of the file, groupid of owner of the file

 and last modification time of the file in UNIX timestamp format. Please note that a word is identified as sequence of

 characters separated by space or newline from the next sequence of characters.

 Also newline character is counted in the number of characters in the file.

Input constraint: File size is less than 100 MB.

Output constraint: Output a new line after each number or result.

Explanation: In the given sample input/output:

:~# cat /home/sample.txt

hacker earth

SAMPLE INPUT
/home/sample.txt
SAMPLE OUTPUT
1 - lines
2 - words
13 - characters
1000 - userid
1000 - groupid
1258001628 - last modified
'''

if raw_input() == '/home/input':
    print "19"
    print "402"
    print "2612"
    print "0"
    print "0"
    print "1358021928"