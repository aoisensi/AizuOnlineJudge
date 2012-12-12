#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=541165
while True:
    H, W = [int(i) for i in raw_input().split()]
    if H == 0 and W == 0:
        break
    for i in range(H):
        if i == 0 or i == H - 1:
            print '#' * W
        else:
            print '#' + '.' * (W - 2) + '#'
    print