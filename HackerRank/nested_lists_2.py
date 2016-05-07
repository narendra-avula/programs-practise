__author__ = 'Hinshitsu-IT'
'''
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Berry
Harry
'''
h={}
N=int(input())
for i in range(N):
	a= input().rstrip()
	b= float(input())
	if b not in h: h[b]=[]
	h[b].append(a)

keys=sorted(h.keys())

for e in sorted(h[keys[1]]):
    print(e)