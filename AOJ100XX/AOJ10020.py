#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=541825
string = ''
while True:
    try:
        string += raw_input()
    except EOFError:
        break
string = string.lower()
a = ord('a')
for i in range(a, a+26):
    print chr(i), ':', string.count(chr(i))