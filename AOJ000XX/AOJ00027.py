#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=551019
import datetime
week = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]
while True:
    (m, d) = [int(i) for i in raw_input().split()]
    if m == 0:
        break
    dt = datetime.datetime(2004, m, d)
    print week[dt.weekday()]