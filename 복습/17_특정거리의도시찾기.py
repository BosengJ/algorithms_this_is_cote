# p339 특정 거리의 도시 찾기

# n,m,k,x = map(int,input("공백을 기준으로 n,m,k,x를 입력하세요:").split())
# information = []
# for i in range(m):
#     information.append(list(map(int,input("도시A에서 도시B로의 도로를 공백으로 구분하여 A,B를 입력하세요:").split())))

n,m,k,x = 4,4,2,1
information = [[1, 2], [1, 3], [2, 3], [2, 4]]

road = [[]] * (n+1)
for i in range(m):
    idx = information[i][0]
    v = information[i][1]
    print(idx,v)
print(road)



# a = []
# b = 1
# if (len(a) == 0) or (b < a[0]):
#     a.append(b)

# print(a)