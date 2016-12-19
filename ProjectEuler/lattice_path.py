__author__ = 'narendra'

def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1),1)

n = 20
m = 20
print n, "x", m, "rectangular grid", ( factorial(n+m) ) // ( factorial(n) * factorial(m) )