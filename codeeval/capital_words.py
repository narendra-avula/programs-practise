__author__ = 'Hinshitsu-IT'
'''
Hello world
javaScript language
a letter
1st thing

Hello World
JavaScript Language
A Letter
1st Thing
'''


fhand = open('capital_words.txt','r')
for line in fhand:
    # print(' '.join(str(i).capitalize() for i in list(map(str, line.strip().split()))))
    print(' '.join((i[0].capitalize() + i[1:] for i in line.split())))