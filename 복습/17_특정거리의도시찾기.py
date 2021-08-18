# p339 특정 거리의 도시 찾기

from collections import deque

# n,m,k,x = map(int,input("공백을 기준으로 n,m,k,x를 입력하세요:").split())
# city = []
# for i in range(m):
#     city.append(list(map(int,input("도시A에서 도시B로의 도로를 공백으로 구분하여 A,B를 입력하세요:").split())))

n,m,k,x = 4,4,2,1
city = [[1, 2], [1, 3], [2, 3], [2, 4]]

# city -> city node 로 바꿔주는 코드
city_node = []
for c in range(n+1):
    node = []
    for i in range(m):
        for j in range(2):
            if (j == 0) and (city[i][j] == c):
                node.append(city[i][j+1])
    city_node.append(node)
print("city_node:", city_node)

# 최단거리 dictionary 생성
city_dict = dict()
k = 1
for i in range(n):
    city_dict[k] = []
    k += 1
print("city_dict", city_dict)

# bfs
q = deque([])
q.append([x,0])
while q:
    print(q)
    idx,cnt = q.popleft()
    city_dict[idx].append(cnt)
    tmp = city_node[idx]
    for n in tmp:
        q.append([n,cnt+1])
print(city_dict)

for k,v in city_dict.items():
    if len(v) > 1:
        m = min(v)
        city_dict[k] = [m]
print(city_dict)

    
    



# a = []
# b = 1
# if (len(a) == 0) or (b < a[0]):
#     a.append(b)

# print(a)