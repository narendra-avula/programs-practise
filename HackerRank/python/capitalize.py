__author__ = 'narendra'
'''
You are given a string . Your task is to capitalize each word of .

Input Format

A single line of input containing the string, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

hello world
Sample Output

Hello World
'''


def capitalize(string):
    words = list(string.split())
    return ' '.join(word.capitalize() for word in words)



if __name__ == '__main__':
    string = raw_input()
    capitalized_string = capitalize(string)
    print capitalized_string