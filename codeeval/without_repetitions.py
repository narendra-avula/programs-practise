__author__ = 'Hinshitsu-IT'
'''
But as he spake he drew the good sword from its scabbard, and smote a heathen knight, Jusssstin of thee Iron Valley.
'''
fhand = open('without_repetitions.txt','r')
for line in fhand:
    words = line.split()
    new_words = []
    for string in words:
        new_string = ''
        for i in range(len(string)-1):
            if string[i] != string[i+1]:
                new_string = new_string+string[i]
        new_string = new_string + string[-1]
        new_words.append(new_string)
    print(' '.join(new_words))


# string = 'Shellless mollusk lives in wallless house in wellness. Aaaarrghh!'
# string = string.split()
# new_string = []
# for word in string:
#     new_word = []
#     for i in range(len(word)-1):
#         if word[i] != word[i+1]:
#             new_word.append(word[i])
#     if word[-1] == word[-2]:
#         new_word.append(word[-2])
#     if word[-1] != word[-2]:
#         new_word.append(word[-1])
#     new_string.append(''.join(new_word))
# print(' '.join(str(i) for i in new_string))


