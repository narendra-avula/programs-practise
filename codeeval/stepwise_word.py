__author__ = 'Hinshitsu-IT'
'''
cat dog hello
stop football play
music is my life

h *e **l ***l ****o
f *o **o ***t ****b *****a ******l *******l
m *u **s ***i ****c
'''

fhand = open('stepwise_word.txt','r')
for line in fhand:
    string = max(line.strip().split(),key=len)
    # print(string)
    new_string = string[0]+ ' '
    for i in range(1,len(string)):
        new_string = new_string +'*'*i+ string[i] + ' '
    print(new_string)