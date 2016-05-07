__author__ = 'Hinshitsu-IT'
'''

'''

def pascal_triangle(rows):
    string = ''
    for rownum in range (rows):
        value=1
        new_list = [value]
        for iteration in range (rownum):
            value = value * ( rownum-iteration ) * 1 / ( iteration + 1 )
            new_list.append(int(value))
        # print(PrintingList)
        string = string  + ' '.join(str(i) for i in new_list)+' '
    return string

test_cases = open('pascal_triangle.txt','r')
for test in test_cases:
    print(pascal_triangle(int(test.strip())))
