__author__ = 'Hinshitsu IT'
#
# for i in range(int(input())):
#     print(i, oct(i), hex(i), bin(i))

# n=int(input())
# d=1
# x=1
# while n>=x:
# 	d+=1
# 	x*=2
# for i in range(1,n+1):
# 	print('%*d%*o%*X'%(d-1,i,d,i,d,i)+bin(i)[2:].rjust(d))

n = int(input())
spacing = len(bin(n)[2:])
for i in range(1,n+1):
    print (str(i).rjust(spacing, ' '),str(oct(i)[2:]).rjust(spacing, ' '),str(hex(i)[2:].upper()).rjust(spacing, ' '),str(bin(i)[2:]).rjust(spacing, ' '))