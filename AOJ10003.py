#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=541129
s = raw_input()
sr = s.split()
a = int(sr[0])
b = int(sr[1])
if(a<b):
    print 'a < b'
elif(a>b):
    print 'a > b'
else:
    print 'a == b'