# p92 큰 수의 법칙
# n,m,k = map(int,input("n,m,k 를 공백을 구분으로 입력하세요:").split())
# num = list(map(int,input("배열의 숫자를 공백을 구분으로 입력하세요:").split()))

n,m,k = 5,8,3
num = [2, 4, 5, 4, 6]

def bubbleSort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] < li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    return li

descending_num = bubbleSort(num)

answer, cnt = 0,0
for i in range(m):
    if cnt < k:
        answer += descending_num[0]
        cnt += 1
    else:
        answer += descending_num[1]
        cnt = 0
print(answer)
