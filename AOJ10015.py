#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=541176
loop = int(raw_input())
have_card = []
for i in range(loop):
    have_card.append(raw_input())
for i in range(4):
    if i == 0:
        g = 'S'
    elif i == 1:
        g = 'H'
    elif i == 2:
        g = 'C'
    elif i == 3:
        g = 'D'
    for j in range(1, 14):
        card = g + ' ' + str(j)
        if not card in have_card:
            print card