#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=551256
while True:
    try:
        g = int(raw_input())
    except:
        break
    for i in [2**j for j in xrange(10)]:
        if(g & i):
            print i,
    print