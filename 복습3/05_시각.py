# input
n = int(input("정수 n을 입력하세요 >"))

# 3이 있을 때 마다 cnt +1 한다
cnt = 0
for hour in range(n+1):
    for min in range(60):
        for sec in range(60):
            if '3' in str(hour) + str(min) + str(sec):
                cnt += 1

print(cnt)

