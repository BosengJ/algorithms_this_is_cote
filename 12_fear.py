n = map(int,input("모험가 N명을 입력하세요"))
fears = list(map(int,input("공포도를 공백을 기준으로 입력하세요").split()))

def ascending(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

fears_sorted = ascending(fears)
cnt, group = 0,0

for fear in fears_sorted:
    cnt += 1
    if fear == cnt:
        group += 1
        cnt = 0
print(group)

# 모험가 길드
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