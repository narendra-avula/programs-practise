__author__ = 'Naidu'
'''
You are given a string S. S consists of several words separated by one or more spaces. Word consists of Latin letters as well as other symbols (but not spaces).
In each word which starts from lowercase Latin letter replace starting letter with uppercase Latin letter.

Input
The only line contains S

Output
Output one line with modified string S.

Constraints
1 <= length of S <= 30 000

SAMPLE INPUT
Wish you were here
SAMPLE OUTPUT
Wish You Were Here
'''

words = raw_input().split()
new_words = []
new_word = ''
for word in words:
    new_word = word[0].upper() + word[1:]
    new_words.append(new_word)
print ' '.join(word for word in new_words)