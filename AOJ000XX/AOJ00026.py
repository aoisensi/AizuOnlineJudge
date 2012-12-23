#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=551011
cell = [[0] * 10 for i in xrange(10)]

large = [[0,0,1,0,0],
         [0,1,1,1,0],
         [1,1,1,1,1],
         [0,1,1,1,0],
         [0,0,1,0,0]]

medium= [[0,0,0,0,0],
         [0,1,1,1,0],
         [0,1,1,1,0],
         [0,1,1,1,0],
         [0,0,0,0,0]]

small = [[0,0,0,0,0],
         [0,0,1,0,0],
         [0,1,1,1,0],
         [0,0,1,0,0],
         [0,0,0,0,0]]

size = [0,small,medium,large]

while True:
    try:
        x, y, s = [int(i) for i in raw_input().split(',')]
    except EOFError:
        break
    except ValueError:
        break
    p = size[s]
    for i in xrange(5):
        for j in xrange(5):
            px = i+x-2
            py = j+y-2
            if(px in xrange(10) and py in xrange(10)):
                cell[py][px] += p[i][j]
print reduce(lambda x,y:x+y,map(lambda x:x.count(0),cell))
print max(map(max,cell))