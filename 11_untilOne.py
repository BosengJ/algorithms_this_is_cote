n,k = map(int,input("n,k를 공백을 구분으로 입력하세요:").split())

cnt = 0
while n != 1:
    if n % k == 0:
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)
