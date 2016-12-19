__author__ = 'narendra'

filename = 'p022_names.txt'

def read_file(filename):
    words_string = ''
    with open(filename, "r") as f:
        for line in f:
            words_string = line.replace('"',"")
    return words_string.split(",")

def keys_dict():
    keys = {chr(ele+65): ele+1 for ele in xrange(26)}
    return keys

def calculate_score(word, number):
    keys = keys_dict()
    word_score = 0
    for char in word:
        word_score += keys[char]
    print word, word_score, number, word_score * number
    return word_score * number


def main():
    words = read_file(filename)
    words.sort()
    scores = 0
    for i in range(0,len(words)):
        # number = i+1
        # print i+1, words[i]
        scores += calculate_score(words[i], i+1)
    return scores


print main()

# print read_file(filename)
# print keys_dict()
