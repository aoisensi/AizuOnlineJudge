#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=549859
for i in range(int(raw_input())):
    (x1, y1, x2, y2, x3, y3, x4, y4) = map(float,raw_input().split())
    x1 -= x2
    y1 -= y2
    x3 -= x4
    y3 -= y4
    if(x1 == 0 or x3 == 0):
        if(x1 == 0 and x3 == 0):
            print 'YES'
        else:
            print 'NO'
    else:
        if(y1 / x1 == y3 / x3):
            print 'YES'
        else:
            print 'NO'