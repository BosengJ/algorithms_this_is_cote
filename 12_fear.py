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