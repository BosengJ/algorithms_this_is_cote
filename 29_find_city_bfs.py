# p339 특정 거리의 도시 찾기
# sys.stdin.readline()으로 input을 받아야한다

from collections import deque
import sys

# n,m,k,x = map(int, input("n,m,k,x을 공백을 구분으로 입력하세요:").split())
# city = []
# for i in range(m):
#     city.append(list(map(int,sys.stdin.readline("도시의 정보를 입력하세요:").split())))

n,m,k,x = 4,4,2,1
city = [[1, 2], [1, 3], [2, 3], [2, 4]]

# 각 도시별(key) 최단 거리(value)를 나타내는 사전 만들기
city_dict = {}
c = 1
for i in range(n):
    city_dict[c] = []
    c += 1

# 출발도시 x 최단거리 값 처리
city_dict[x].append(0)

# 출발도시 x 를 기준으로 최단거리 구하기
distance = 1
for i in range(m):
    for j in range(2):
        if (j == 0) and (city[i][j] == x):
            arrival = city[i][j+1]
            city_dict[arrival].append(distance)

print(city_dict)