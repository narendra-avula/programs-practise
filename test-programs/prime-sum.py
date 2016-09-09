

def sieve(n):
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)

def prime_sum(A):
    pass

number = 16
list_numbers = sieve(number)
print list_numbers
for i in range(len(list_numbers)):
    for j in range(len(list_numbers)-1):
        if list_numbers[j] > list_numbers:
            pass



