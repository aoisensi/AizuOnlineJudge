#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=551244
def dfs(n, sum ,depth):
    if(depth == 0):
        return int(sum == s)
    else:
        count = 0
        for i in xrange(n+1,10):
            count += dfs(i, sum+i, depth-1)
        return count

while True:
    (n, s) = [int(i) for i in raw_input().split()]
    if((0,0) == (n,s)):
        break
    print dfs(-1,0,n)