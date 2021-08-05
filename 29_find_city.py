# p339

n,m,k,x = map(int, input("n,m,k,x을 공백을 구분으로 입력하세요:").split())
city = []
for i in range(m):
    city.append(list(map(int,(input("도시의 정보를 입력하세요:").split()))))


print(city)
