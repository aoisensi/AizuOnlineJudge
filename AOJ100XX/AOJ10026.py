#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=542449
import math
while True:
    if raw_input() == '0':
        break
    l = [float(i) for i in raw_input().split()]
    m = reduce(lambda x, y: x + y, l) / len(l)
    a1 = map(lambda x: (x - m) ** 2, l)
    a2 = reduce(lambda x, y: x + y, a1) / len(a1)
    print math.sqrt(a2)