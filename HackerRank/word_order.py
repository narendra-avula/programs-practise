__author__ = 'Hinshitsu IT'
'''

4
bcdef
abcdefg
bcde
bcdef

3
2 1 1

# '''
# N = int(input())
# mylist = [input() for _ in range(N)]
# x = set(mylist)
# print (len(x))
# for i in x:
#     print(mylist.count(i),end=' ')


# h={}
# for i in range(int(input())):
# 	s= input().rstrip()
# 	if s not in h: h[s] = [i,0]
# 	h[s][1] += 1
#
# print(len(h))
# print(' '.join(str(e[1]) for e in sorted(h.values())))

N=int(input())
dict={}
li=[]
for i in range(N):
    word= input()
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
        li.append(word)
print (len(li))
for i in li:
    print (dict[i],end=' ')