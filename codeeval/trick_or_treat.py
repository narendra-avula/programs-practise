__author__ = 'CustomFurnish'


with open('trick_or_treat.txt') as test_cases:
    for test in test_cases:
        # print(test)
        candies = [int(e.split(':')[1]) for e in test.split(',') ]
        # print(candies)
        total = sum(candies[3] * c * i for c , i in zip(candies[:-1],(3,4,5)))
        # print(total)
        print(total//sum(candies[:-1]))





        # p = [int(e.split(':')[1]) for e in test.split(',')]
        # print(p)
        # print(p[:-1])
        # s = sum(p[3] * c * i for c, i in zip(p[:-1], (3, 4, 5)))
        # print(s // sum(p[:-1]))