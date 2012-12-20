#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=549107
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

while True:
    try:
        (x1, y1, x2, y2, x3, y3, xp, yp) = map(float, raw_input().split())
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        p3 = Point(x3, y3)
        pp = Point(xp, yp)
        p12 = p1 - p2
        p23 = p2 - p3
        p31 = p3 - p1
        pp1 = pp - p1
        pp2 = pp - p2
        pp3 = pp - p3
        c1 = (p12 * pp1 < 0.0)
        c2 = (p23 * pp2 < 0.0)
        c3 = (p31 * pp3 < 0.0)
        if(c1 ^ c2 or c2 ^ c3):
            print 'NO'
        else:
            print 'YES'
    except EOFError:
        break