# food_time = list(map(int,input("공백을 기준으로 각 음식을 모두 먹는 데 필요한 시간을 입력하세요").split()))
# k = int(input("방송이 중단된 시간을 입력하세요"))

food_time = [3,1,2]
k = 5
while True:
    for i in range(len(food_time)):
        if food_time[i] > 0:
            food_time[i] -= 1
            k -= 1
        if k == 0:
            answer = i+1
            break

print(food_time)
print(k)       

        

