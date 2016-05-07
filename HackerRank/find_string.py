__author__ = 'Hinshitsu IT'

string = input()
sub_string = input()
def count(s, sub):
    result = 0
    for i in range(len(s) + 1 - len(sub)):
        result += (s[i:i + len(sub)] == sub)
    return result
print(count(string, sub_string))
