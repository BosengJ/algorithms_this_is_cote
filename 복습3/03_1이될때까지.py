# input
n,k = map(int,input("n, k를 공백으로 구분하여 입력하세요 (단, n은 항상 k보다 크거나 같아야 합니다) >").split())

cnt = 0
while n > 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1
    cnt += 1

print(cnt)