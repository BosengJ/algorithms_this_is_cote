# p99 1이 될 때까지

n,k = map(int,input("n,m 을 공백을 구분으로 입력하세요:").split())

cnt = 0
while n != 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1
    cnt += 1
print(cnt)