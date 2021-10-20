# p315 볼링골 고르기

n,m = map(int,input("공백을 기준으로 n,m을 입력하세요:").split())
balls = list(map(int,input("공백을 기준으로 각 볼링골의 무게를 입력하세요:").split()))

answer = 0
for i in range(len(balls)-1):
    for j in range(i+1,len(balls)):
        if balls[i] != balls[j]:
            answer += 1
print(answer)