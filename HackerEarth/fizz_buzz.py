__author__ = 'Hinshitsu-IT'

'''
2
3 15

1
2
Fizz
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
'''

for _ in range(int(input())):
    numbers_list = map(int, input().split())
    for i in numbers_list:
        print(i)
        for number in range(i):
            print(number)
            if number % 5 == 0 and number % 3 == 0:
                print('FizzBuzz')
            elif number % 5 == 0:
                print('Fizz')
            elif number % 3 == 0:
                print('Buzz')
            else:
                print(number)