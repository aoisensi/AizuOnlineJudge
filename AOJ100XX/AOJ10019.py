#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=541820
while True:
    ints = [int(i) for i in raw_input()]
    if ints == [0]:
        break
    print reduce(lambda a, b: a + b, ints)