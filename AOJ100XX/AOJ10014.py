#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=541173
while True:
    H, W = [int(i) for i in raw_input().split()]
    if H == 0 and W == 0:
        break
    for i in range(H):
        line = ''
        for j in range(W):
            if (i + j) & 1:
                line += '.'
            else:
                line += '#'
        print line
    print