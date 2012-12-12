#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=542439
import math
a, b, C = [float(i) for i in raw_input().split()]
R = C / 180 * math.pi
print (a * b * math.sin(R)) / 2
print a + b + math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(R))
print b * math.sin(R)