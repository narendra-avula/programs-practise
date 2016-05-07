__author__ = 'Hinshitsu-IT'



for i in range(int(input())):
    numbers = []
    for num in range(2,664580):
       # prime numbers are greater than 1
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               numbers.append(num)

    number_index = int(input())
    print(numbers[number_index-1])