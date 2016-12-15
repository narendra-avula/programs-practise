__author__ = 'narendra'


def check_pathagorean(a, b, c):
    return (a**2) + (b**2) == (c**2)

SUM = 1000

for i in range(1, SUM):
    for j in range(i+1, SUM):
        c = SUM - (i + j)
        if(check_pathagorean(i, j, c)):
            print i, j, c
            print i * j * c
            break