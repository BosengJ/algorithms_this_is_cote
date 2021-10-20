# input
n,m,k = map(int,input("n,m.k를 공백으로 구분하여 입력하세요 >").split())
nums = list(map(int,input("공백으로 구분하여 숫자를 입력하세요 >").split()))

# test case
# n,m,k = 5,8,3
# nums = [2,4,5,4,6]

# 내림차순으로 정렬하는 함수를 구현하여 주어진 자연수들을 정렬해준다.
def MaxToMin(li):
    for i in range(len(li)):
        for j in range(len(li)-i-1):
            if li[j] < li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

new_nums = MaxToMin(nums[:])


# 주어진 수들을 m번 더하여 가장 큰 수를 만드는 반복문 구현
# 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 k번을 초과하여 더해질 수 없다.
mcnt,kcnt,answer = 0,0,0
while mcnt < m:
    if kcnt < k:
        answer += new_nums[0]
        kcnt += 1
        mcnt += 1
    else:
        answer += new_nums[1]
        kcnt = 0
        mcnt += 1

print(answer)