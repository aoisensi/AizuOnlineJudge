#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=551300
class Point(object):
    x = 0.0
    y = 0.0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(left, right):
        return Point(left.x - right.x, left.y - right.y)
    #cross
    def __mul__(left, right):
        return left.x * right.y - left.y * right.x
def f(n):
    return n<0
while True:
    try:
        (xa,ya,xb,yb,xc,yc,xd,yd) = [float(i) for i in raw_input().split(',')]
        a = Point(xa,ya)
        b = Point(xb,yb)
        c = Point(xc,yc)
        d = Point(xd,yd)
        ab = a - b
        bc = b - c
        cd = c - d
        da = d - a
        if((f(ab*bc) + f(bc*cd)) + (f(cd*da) + f(da*ab)) in (0,4)):
            print 'YES'
        else:
            print 'NO'
    except:
        break