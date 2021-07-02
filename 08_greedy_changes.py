# p87 예제3-1 거스름돈

n = input("잔돈입력:")

coins = [500,100,50,10]
cnt = 0
for coin in coins:
    p,q = divmod(int(n),coin)
    cnt += p
    n = q
    if n == 0:
        break
print(cnt)
