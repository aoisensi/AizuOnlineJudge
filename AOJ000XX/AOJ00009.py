#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=543495
N = 10 ** 6
sieve = map(lambda x:False, range(2, N + 1))
for i in range(2, N + 1):
    if sieve[i - 2]:
        continue
    for j in range(i * 2, N + 1, i):
        sieve[j - 2] = True
while True:
    try:
        n = int(raw_input())
    except EOFError:
        break
    print sieve[:n - 1].count(False)