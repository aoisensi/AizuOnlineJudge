#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=541130
s = raw_input()
sr = s.split()
ints = []
for ss in sr:
    ints.append(int(ss))
ints.sort()
for i in ints:
    print i,
print