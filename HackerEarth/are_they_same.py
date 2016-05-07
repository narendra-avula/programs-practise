__author__ = 'Hinshitsu-IT'
'''
mindsweepers
swrepeesdnim

YES
'''
text = list(input())
reverse_text = list(input())
count = 0
for i in range(len(text)):
    if text[i] in reverse_text:
        count += 1

if count == len(text):
    print('YES')
else:
    print('NO')