#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=551090
words = raw_input().split()
dict = {}
for word in words:
    try:
        dict[word] += 1
    except:
        dict[word] = 1
print max(dict.items(),key=lambda x:x[1])[0],
print max(words, key=len)