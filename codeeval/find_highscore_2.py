__author__ = 'Hinshitsu-IT'
'''
72 64 150 | 100 18 33 | 13 250 -6
10 25 -30 44 | 5 16 70 8 | 13 1 31 12
100 6 300 20 10 | 5 200 6 9 500 | 1 10 3 400 143

100 250 150
13 25 70 44
100 200 300 400 500
'''
def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0

  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg

  return out

string = '100 6 300 20 10 | 5 200 6 9 500 | 1 10 3 400 143'

string = string.split('|')
for i in string:
    i = [int(i) for i in i.split()]
    print(i)





