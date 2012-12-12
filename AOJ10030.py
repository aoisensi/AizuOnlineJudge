#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=543320
raw_input()
S = map(int, raw_input().split())
raw_input()
T = map(int, raw_input().split())
count = 0
for i in T:
    if(i in S):
        count += 1
print count