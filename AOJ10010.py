#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=541154
while True:
    string = raw_input()
    strings = string.split()
    a = int(strings[0])
    op = strings[1]
    b = int(strings[2])
    if op == '?':
        break
    elif op == '+':
        print a + b
    elif op == '-':
        print a - b
    elif op == '*':
        print a * b
    elif op == '/':
        print a / b