#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=543341
mountain = []
removed = []
while True:
    command = raw_input()
    if command.split()[0] == 'push':
        mountain.append(command.split()[1])
    elif command.split()[0] == 'pop':
        removed.append(mountain[-1])
        mountain.pop(-1)
    elif command.split()[0] == 'quit':
        break
for block in removed:
    print block