#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=549125
from collections import deque
garage = deque()
while True:
    try:
        came = int(raw_input())
        if came == 0:
            print garage.pop()
        else:
            garage.append(came)
    except ValueError:
        break