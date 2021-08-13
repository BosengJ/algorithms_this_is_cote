# p339 특정 거리의 도시 찾기

# n,m,k,x = map(int,input("공백을 기준으로 n,m,k,x를 입력하세요:").split())
# city = []
# for i in range(m):
#     city.append(list(map(int,input("도시A에서 도시B로의 도로를 공백으로 구분하여 A,B를 입력하세요:").split())))

n,m,k,x = 4,4,2,1
city = [[1, 2], [1, 3], [2, 3], [2, 4]]

city_node = []
for c in range(n+1):
    node = []
    for i in range(m):
        for j in range(2):
            if (j == 0) and (city[i][j] == c):
                node.append(city[i][j+1])
    city_node.append(node)
print(city_node)


# a = []
# b = 1
# if (len(a) == 0) or (b < a[0]):
#     a.append(b)

# print(a)