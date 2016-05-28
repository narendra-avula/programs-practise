__author__ = 'Narendra'
'''
Write a command line tool which takes a file path as input and prints the number of lines, number of words,

number of characters in the file, userid of the owner of the file, groupid of owner of the file and

last modification time of the file in UNIX timestamp format. Please note that a word is identified as

sequence of characters separated by space or newline from the next sequence of characters. Also newline

character is counted in the number of characters in the file.

Input constraint: File size is less than 100 MB.

Output constraint: Output a new line after each number or result.

Explanation: In the given sample input/output:

:~# cat /home/sample.txt

SAMPLE INPUT
/home/sample.txt

SAMPLE OUTPUT
1       prints the number of lines
2       number of words
13      number of characters in the file
1000    userid of the owner of the file
1000    groupid of owner of the file
1258001628  last modification time of the file in UNIX timestamp format
'''

# file_path = raw_input()
file_path = 'C:\Users\Narendra\Desktop\sample.txt'
file_open = open(file_path, 'r')
# print file_open
num_lines = 0
num_words = 0
num_chars = 0
for line in file_open:
    words = line.split()
    num_lines += 1
    num_words += len(words)
    num_chars += len(line)

print num_lines
print num_words
print num_chars
