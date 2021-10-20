# input
n,m = map(int,input("행의 개수 n과 열의 개수 m을 공백을 기준으로 하여 입력하세요 >").split())
cards = []
for i in range(n):
    cards.append(list(map(int,input("n개의 줄에 걸쳐 각 카드에 적힌 숫자를 공백으로 구분하여 입력하세요 >").split())))

# test
# n,m = 3,3
# cards = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]

# 가장 작은 숫자를 뽑아내는 함수
def checkMin(li):
    minNum = li[0]
    for i in range(len(li)):
        if li[i] < minNum:
            minNum = li[i]
    return minNum

# 가장 큰 숫자를 뽑아내는 함수
def checkMax(li):
    maxNum = li[0]
    for i in range(len(li)):
        if li[i] > maxNum:
            maxNum = li[i]
    return maxNum

# 각 행의 가장 작은 수를 찾아내서 리스트로 return 해주는 함수
def findMinCardNum(li):
    nums = []
    for i in range(len(li)):
        card_min_num = checkMin(li[i])
        nums.append(card_min_num)
    return nums

n_min_nums = findMinCardNum(cards)
answer = checkMax(n_min_nums)

print(answer)