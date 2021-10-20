# input
# n,m,k = map(int,input("n,m.k를 공백으로 구분하여 입력하세요 >").split())
# nums = list(map(int,input("공백으로 구분하여 숫자를 입력하세요 >").split()))

# test case
n,m,k = 5,8,3
nums = [2,4,5,4,6]

# 오름차순으로 정렬하는 함수
def MinToMax(li):
    for i in range(len(li)):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li