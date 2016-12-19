__author__ = 'narendra'


def longest_collatz(number):
    sequence = []
    while number > 0:
        if ( number % 2 ) == 0 :
            number = number/2
            sequence.append(number)
        else:
            number = ( 3 * number ) + 1
            sequence.append(number)

    return sequence

def collatz_sequence(x):
    seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x= x/2
       else:
         x= 3*x+1
       seq.append(x)
    return seq


def main():
    start_number = None
    start_number_length = None
    for i in range(1,1000000):
        print i
        length = len(collatz_sequence(i))
        if start_number is None or length > start_number_length:
            start_number = i
            start_number_length = length

    return start_number, start_number_length


import time

start_time = time.time()
print main()
print("--- %s seconds ---" % (time.time() - start_time))


# print longest_collatz(13)
# print collatz_sequence(9)
# print collatz_sequence(6)


