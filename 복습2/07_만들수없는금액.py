# p314 만들 수 없는 금액

# n = int(input("동전의 개수 n을 입력하세요:"))
# coins = list(map(int,input("공백을 기준으로 각 동전의 화폐 단위를 나타내는 자연수를 입력하세요:").split()))

n = 5
coins = [3, 2, 1, 1, 9]

def bubbleSort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    return li

sorted_coins = bubbleSort(coins)
min_coin = 1
for coin in sorted_coins:
    if min_coin < coin:
        break
    else:
        min_coin += coin
print(min_coin)