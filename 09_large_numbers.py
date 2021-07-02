# 첫번째 방법
n,m,k = map(int,input("숫자 3개를 공백을 구분으로 입력하세요:").split())
arr = list(map(int,input("배열을 공백을 구분으로 입력하세요:").split()))

def bubbleSort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] < li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

descending_arr = bubbleSort(arr)
cnt, large_num = 0,0
for i in range(m):
    if cnt < k:
        large_num += descending_arr[0]
        cnt += 1
    else:
        large_num += descending_arr[1]
        cnt = 0
print(large_num)

# 수학적 아이디어를 사용한 두번째 방법
# n,m,k = map(int,input("숫자 3개를 공백을 구분으로 입력하세요:").split())
# arr = list(map(int,input("배열을 공백을 구분으로 입력하세요:").split()))

# def bubbleSort(li):
#     for i in range(len(li)-1):
#         for j in range(len(li)-i-1):
#             if li[j] < li[j+1]:
#                 li[j], li[j+1] = li[j+1], li[j]
#     return li

# descending_arr = bubbleSort(arr)

# # 가장 큰 수를 더하는 횟수
# cnt = ((m//(k+1)) * k) + (m % (k+1))

# large_num = 0
# large_num += cnt * descending_arr[0]
# large_num += (m-cnt) * descending_arr[1]

# print(large_num)
