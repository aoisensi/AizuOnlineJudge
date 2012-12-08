#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=541148
a, b = [int(i) for i in raw_input().split()]
print "%d %d %f" % (a/b, a%b, float(a)/b)