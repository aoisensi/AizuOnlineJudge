#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=544028
w = int(raw_input())
n = int(raw_input())
a = []
for i in range(n):
    a.append(map(int, raw_input().split(',')))
r = range(1, w + 1)
for i in a:
    tmp = r[i[0] - 1]
    r[i[0] - 1] = r[i[1] - 1]
    r[i[1] - 1] = tmp
for i in r:
    print i