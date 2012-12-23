#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=551288
def dfs(al,bl,cl):
    if(len(al) == 0):
        return True
    else:
        if(al[0] > bl[-1]):
            b = dfs(al[1:], bl+al[0:1], cl)
            if(b):
                return True
        if(al[0] > cl[-1]):
            b = dfs(al[1:], bl, cl+al[0:1])
            if(b):
                return True
        return False

for i in xrange(int(raw_input())):
    if(dfs([int(j) for j in raw_input().split()],[-1],[-1])):
        print 'YES'
    else:
        print 'NO'