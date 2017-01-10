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

import os

def get_file_stats(file_path):
    lines = words = chars = 0
    with open(file_path, 'r') as in_file:
        for line in in_file:
            lines += 1
            words += len(line.split())
            chars += len(line)

    stats_file = os.stat(file_path)
    print lines
    print words
    print chars
    print stats_file.st_uid
    print stats_file.st_gid
    print int(stats_file.st_mtime)

if __name__ == '__main__':
    # file_path = '/home/narendra/programs-practise/HackerEarth/tracks/basic-programming/implementation/file-statistics.txt'
    file_path = raw_input()
    values = get_file_stats(file_path)