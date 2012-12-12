#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=542427
word = raw_input().lower()
text = []
while True:
    line = raw_input()
    if line == 'END_OF_TEXT':
        break
    else:
        text += line.lower().split()
print text.count(word)