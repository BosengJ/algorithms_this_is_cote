# p96 숫자 카드 게임

n,m = map(int,input("n,m 을 공백을 구분으로 입력하세요:").split())
cards = []
for i in range(n):
    cards.append(list(map(int,input("카드에 적힌 숫자를 공백을 구분으로 입력하세요:").split())))

# n,m = 3,3
# cards = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]

min_cards = []
for c in cards:
    tmp = min(c)
    min_cards.append(tmp)

answer = 0
for c in min_cards:
    if c > answer:
        answer = c


print(answer)