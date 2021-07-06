n = int(input("동전 n개를 입력하세요"))
coins = list(map(int,input("공백을 기준으로 동전 단위를 입력하세요").split()))

def coinSort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

sorted_coins = coinSort(coins)
print(sorted_coins)
min_coin = 1
for coin in sorted_coins:
    if min_coin < coin:
        break
    else:
        min_coin += coin
print(min_coin)