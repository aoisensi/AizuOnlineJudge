#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=542436
import math
x1, y1, x2, y2 = [float(i) for i in raw_input().split()]
print math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)
