#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=549892
while True:
    try:
        v = float(raw_input())
    except EOFError:
        break
    print int((((1/9.8)*v)**2)*4.9)/5+2