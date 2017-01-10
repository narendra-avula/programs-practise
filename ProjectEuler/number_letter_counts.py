__author__ = 'narendra'
import time

number_0_9 = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
number_10_19 = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
number_tens =  {20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}

def number_to_letters(number):
    if len(str(number)) == 1:
        return number_0_9[number]
    elif number > 9 and number < 20:
        return number_10_19[number]
    elif number > 19 and number < 100:
        return number_tens[(number/10)*10] +"-" + number_0_9[number % 10]
    else:
        return "more than 100"

def main():
    print number_to_letters(50)

main()


# start_time = time.time()
# main()
# print("--- %s seconds ---" % (time.time() - start_time))
