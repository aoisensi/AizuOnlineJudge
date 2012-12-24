#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=551675
dict = [771,16843009,15,131841,387,33153,1539]
while True:
    cell = reduce(lambda x,y:x+y,map(lambda x:int(raw_input(),2)<<(8*x),xrange(8)))
    for i in [cell >> j for j in xrange(255)]:
        try:
            print chr(dict.index(i) + ord('A'))
        except ValueError:
            continue
    try:
        raw_input()
    except:
        break