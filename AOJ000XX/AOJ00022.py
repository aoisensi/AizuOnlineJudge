#http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=549887
while True:
    n = int(raw_input())
    if n == 0:
        break
    numbers = [int(raw_input()) for i in range(n)]
    if max(numbers) <= 0:
        print max(numbers)
    else:
        ans = 0
        for i in range(n):
            tmp = 0
            for j in range(i,n):
                tmp += numbers[j]
                if(ans<tmp):
                    ans = tmp
        print ans