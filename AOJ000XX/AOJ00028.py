#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=551071
l = []
c = list([0] * 100)
while True:
    try:
        c[int(raw_input()) - 1] += 1
    except:
        break
m = max(c)
for i in xrange(c.count(m)):
    j = c.index(m)
    print j + 1
    c[j] = 0