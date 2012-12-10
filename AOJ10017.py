#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=541811
while True:
    n, x = [int(i) for i in raw_input().split()]
    if(n == 0 and x == 0):
        break
    count = 0
    for i in range(1, 1 + n):
        for j in range(i, 1 + n):
            for k in range(j, 1 + n):
                if(i != j and j != k and i != k):
                    if (i + j + k) == x:
                        count += 1
    print count