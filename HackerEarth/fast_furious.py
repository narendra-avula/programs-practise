__author__ = 'Hinshitsu-IT'
'''
DOM
Brain


3
1 2 3
1 2 4

Brian
2
'''
n = int(input())
dom = list(map(int,input().split()))
brain = list(map(int,input().split()))
dom_speed = []
brain_speed = []
for i in range(1,n):
	dom_speed.append(abs(dom[i-1]-dom[i]))
	brain_speed.append(abs(brain[i-1]-brain[i]))

print(dom_speed)
print(brain_speed)

if max(brain_speed) > max(dom_speed):
    print('Brian')
    print(max(brain_speed))
elif max(brain_speed) < max(dom_speed):
    print('Dom')
    print(max(dom_speed))
else:
    print('Tie')
