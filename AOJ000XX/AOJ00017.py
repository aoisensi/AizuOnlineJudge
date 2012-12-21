#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=549666
def cipher(char):
    if ord(char) <= ord('y') and ord(char) >= ord('a'):
        return str(chr(ord(char) + 1))
    elif char == 'z':
        return 'a'
    else:
        return char
while True:
    try:
        sent = raw_input()
    except EOFError:
        break
    while((sent.find('the') == -1) and (sent.find('this') == -1) and (sent.find('that') == -1)):
        sent = ''.join(map(cipher, sent))
    print sent