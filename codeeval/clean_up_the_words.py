__author__ = 'Hinshitsu-IT'

import re
fhand = open('clean_up_the_words.txt','r')
for line in fhand:
    print(" ".join(re.findall("[a-zA-Z]+", line.lower())))