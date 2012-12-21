#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=549894
while True:
    try:
        a = raw_input().split()
        b = raw_input().split()
        hit = reduce(lambda x,y:x+y,map(lambda x,y:x==y,a,b))
        blow = reduce(lambda x,y:x+y,map(lambda x:x in b,a)) - hit
        print hit, blow
    except EOFError:
        break