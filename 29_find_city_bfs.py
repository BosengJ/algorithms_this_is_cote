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

# 각 노드가 연결된 정보를 리스트 자료형으로 표현
city_node = []
for c in range(m+1):
    node = []
    for i in range(m):
        for j in range(2):
            if (j == 0) and (city[i][j] == c):
                node.append(city[i][j+1])
    city_node.append(node)
print(city_node)

# 각 도시별(key) 최단 거리(value)를 나타내는 사전 만들기
city_dict = {}
c = 1
for i in range(n):
    city_dict[c] = []
    c += 1

# 초기값으로 출발 도시를 넣어준다
queue = deque([x])
distance = 0

while queue:
    c = queue.popleft()
    city_dict[c] = distance
    for i in city_node[c]:
        queue.append(i)
    distance += 1

print(city_dict)