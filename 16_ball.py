n,m = map(int,input("공백을 기준으로 n과 m을 입력하세요").split())
balls = list(map(int,input("공백을 기준으로 공의 무게를 입력하세요").split()))
# balls = [1,5,4,3,2,4,5,2]

answer = 0
for i in range(len(balls)-1):
    for j in range(i+1,len(balls)):
        if balls[j] != balls[i]:
            answer += 1
print(answer)

