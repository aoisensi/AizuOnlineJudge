#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=549889
import math
for i in range(int(raw_input())):
    (xa, ya, ra, xb, yb, rb) = map(float,raw_input().split())
    dist = math.sqrt((xa-xb)**2 + (ya-yb)**2)
    if dist > ra + rb:
        print 0
    elif dist + rb < ra:
        print 2
    elif dist + ra < rb:
        print -2
    else:
        print 1
