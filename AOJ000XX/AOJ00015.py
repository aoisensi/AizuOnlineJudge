#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=549135
n = long(raw_input())
for i in range(n):
    a = long(raw_input())
    b = long(raw_input())
    c = a + b
    if(len(str(c)) > 80):
        print 'overflow'
    else:
        print c