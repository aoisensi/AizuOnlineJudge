#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=544019
import math
from math import *
for i in range(int(raw_input())):
    (x1, y1, x2, y2, x3, y3) = map(float, raw_input().split())
    a1 = 2 * (x2 - x1)
    b1 = 2 * (y2 - y1)
    c1 = x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2
    a2 = 2 * (x3 - x1)
    b2 = 2 * (y3 - y1)
    c2 = x1 ** 2 - x3 ** 2 + y1 ** 2 - y3 ** 2
    xp = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
    yp = (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)
    r = sqrt((x1 - xp) ** 2 + (y1 - yp) ** 2)
    print '%.3f %.3f %.3f' % (xp, yp, r)