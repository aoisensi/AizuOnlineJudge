#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=541162
while True:
    H, W = [int(i) for i in raw_input().split()]
    if H == 0 and W == 0:
        break
    for i in range(H):
        print '#' * W
    print