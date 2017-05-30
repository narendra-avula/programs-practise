__author__ = 'narendra'


if __name__ == '__main__':
    number = int(raw_input())
    if number % 2 == 0:
        if number in range(2,6) or number > 20:
            print "Not Weird"
        elif number in range(6,21):
            print "Weird"
    else:
        print "Weird"

