__author__ = 'Hinshitsu-IT'
'''

Tom exhibited.
Amy Lawrence was proud and glad, and she tried to make Tom see it in her face - but he wouldn't look.
Tom was tugging at a button-hole and looking sheepish.
Two thousand verses is a great many - very, very great many.
Tom's mouth watered for the apple, but he stuck to his work.

Tom exhibited.
Amy Lawrence was proud and glad, and... <Read More>
Tom was tugging at a button-hole and looking sheepish.
Two thousand verses is a great many -... <Read More>
Tom's mouth watered for the apple, but... <Read More>
'''

test_cases = open('read_more.txt','r')
for test in test_cases:
    string = test.strip()
    if len(string) <= 55:
        print(string)
    else:
        string = string[:40].split()
        del string[-1]
        string = ' '.join(string)
        print(string+'... <Read More>')
