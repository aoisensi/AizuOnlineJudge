#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=551294
while True:
    try:
        values = [int(i) for i in raw_input().split(',')]
    except:
        break
    kukaku = values[:-2]
    aspeed = values[10]
    bspeed = values[11]
    nagasa = reduce(lambda x,y:x+y,kukaku)
    jikan  = float(nagasa) / (aspeed + bspeed)
    ekinag = map(lambda x:reduce(lambda x,y:x+y,kukaku[:x]),xrange(1,11))
    for i, j in enumerate(ekinag):
        if(j >= jikan * aspeed):
            print i+1
            break