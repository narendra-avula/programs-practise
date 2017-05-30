__author__ = 'narendra'


def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


a, b = map(int, raw_input().split())
a_factors = factors(a)
b_factors = factors(b)
print len(list(a_factors.intersection(b_factors)))