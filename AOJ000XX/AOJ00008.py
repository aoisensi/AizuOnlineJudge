#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=543454
while True:
    try:
        n = int(raw_input())
    except EOFError:
        break
    count = 0
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    if a + b + c + d == n:
                        count += 1
    print count