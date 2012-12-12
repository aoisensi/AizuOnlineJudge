#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=543331
raw_input()
S = set(map(int, raw_input().split()))
raw_input()
T = set(sorted(map(int, raw_input().split())))
print len(S) - len(S - T)