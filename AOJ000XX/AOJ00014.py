#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=549134
while True:
    try:
        d = int(raw_input())
    except EOFError:
        break
    if d == 600:
        print 0
    else:
        rects = map(lambda x:d*x*x,range(d, 600, d))
        print reduce(lambda x,y:x+y,rects)