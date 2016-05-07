__author__ = 'Hinshitsu-IT'
'''
2
www.google.com
www.hackerearth.com

7/14
11/19

'''
import sys
if sys.version_info[0]>=3:
    raw_input=input

def anti_vowel(c):
    newstr = c
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in c.lower():
        if x in vowels:
            newstr = newstr.replace(x,"")
    return newstr

for _ in range(int(input())):
    input_string = input()
    # total = len(input_string)
    # print(total)
    browser = input_string.split('.')
    browser_name = browser[1]
    # print(browser_name)
    optimize_browser = anti_vowel(browser_name)
    # print(optimize_browser)
    print(str(len(optimize_browser)+4)+'/'+str(len(input_string)))
