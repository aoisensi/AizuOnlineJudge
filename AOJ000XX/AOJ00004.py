#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=543415
while True:
    try:
        a, b, c, d, e, f = map(float, raw_input().split())
    except EOFError:
        break
    x = (e * c - b * f) / (a * e - b * d)
    y = (-d * c + a * f) / (a * e - b * d)
    print '%.3f %.3f' % (x + 0.00001, y + 0.00001)
