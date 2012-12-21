#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=549674
print reduce(lambda x,y:x*y,map(lambda x:x+1,range(int(raw_input()))))