__author__ = 'Hinshitsu-IT'
'''
abcdefghik
Xa,}A#5N}{xOBwYBHIlH,#W
(ABW>'yy^'M{X-K}q,
6240488

012345678
05
NONE
6240488
'''
alphabets = {'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4', 'f':'5', 'g':'6', 'h':'7', 'i':'8', 'j':'9'}

test_cases = open('hidden_digits.txt','r')
for test in test_cases:
    string = ''
    for char in test:
        if char in alphabets:
            string += alphabets[char]
        if char.isdigit():
            string += char

    if len(string) < 1:
        print ('NONE')
    else:
        print (string)