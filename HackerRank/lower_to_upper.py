__author__ = 'Hinshitsu IT'

new_word = ""
for char in input():
    if char.islower():
        new_word += char.upper()
    elif char.isupper():
        new_word += char.lower()
    else:
        new_word += char
print(new_word)