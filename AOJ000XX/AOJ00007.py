#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=543447
import math
debt = 100000
for i in range(int(raw_input())):
    debt = int(math.ceil((debt * 1.05) / 1000)) * 1000
print debt