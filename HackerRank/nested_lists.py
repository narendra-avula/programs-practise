__author__ = 'Hinshitsu-IT'
'''
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Berry
Harry
'''
# dict_marks = {}
# for _ in range(int(input())):
#     name = input()
#     marks = input()
#     dict_marks[name] = marks
#
# print(dict_marks)

marks_list = []
for _ in range(int(input())):
    name = input()
    marks = input()
    marks_list.append([name, marks])

# print(marks_list)
result = []
for i in range(len(marks_list)):
    print(marks_list[i][0])
