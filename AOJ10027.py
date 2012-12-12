#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=543294
turn = int(raw_input())
taro = hanako = 0
for i in range(turn):
    (t_card, h_card) = raw_input().split()
    if t_card > h_card:
        taro += 3
    elif t_card < h_card:
        hanako += 3
    else:
        taro += 1
        hanako += 1
print taro, hanako