__author__ = 'Hinshitsu-IT'
'''
hello 11001
world 10000
cba 111

HEllO
World
CBA
'''
# x.lower() for x in ["A","B","C"]

fhand = open('string_mask.txt','r')
for line in fhand:
    word, numbers = map(str, line.strip().split())
    result = []
    for w, m in zip(word, numbers):
        if m == '1':
            result.append(w.upper())
        else:
            result.append(w.lower())
    print (''.join(result))


