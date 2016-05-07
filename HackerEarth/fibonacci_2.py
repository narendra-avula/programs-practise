__author__ = 'Hinshitsu-IT'

a=1
b=2
limit = 4 * 1000000
add=2
while a+b<limit:
	c=a+b
	a=b
	b=c
	if b%2==0:
		add+=b
print (add)