# p311 모험가 길드

n = int(input("n을 입력하세요:"))
fears = list(map(int,input("각 모험가의 공포도의 값을 공백으로 구분하여 입력하세요:").split()))

# n = 5
# fears = [2, 3, 1, 2, 2]

def bubbleSort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

sorted_fears = bubbleSort(fears)

cnt, group = 0,0
for fear in sorted_fears:
    cnt += 1
    if fear == cnt:
        group += 1
        cnt = 0
print(group)


# 테스트케이스
# 5
# 2 3 1 2 2
# 답 : 2
# 5
# 5 5 5 5 5
# 답 : 1
# 5
# 7 5 1 6 1
# 답 : 2
# 5
# 1 1 1 1 5
# 답 : 4
# 5
# 2 1 2 1 2
# 답 : 3
# 5
# 4 1 2 3 1
# 답 : 2
# 1
# 3
# 답 : 0
# 1
# 1
# 답 : 1