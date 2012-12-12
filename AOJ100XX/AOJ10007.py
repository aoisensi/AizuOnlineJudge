#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=541135
while True:
    a, b = [int(i) for i in raw_input().split()]
    if a == 0 and b == 0:
        break
    elif a < b:
        print a, b
    else:
        print b, a