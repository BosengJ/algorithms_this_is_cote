n,m = map(int, inut("n,m을 공백을 구분으로 입력하세요:"))
maze = []
for i in range(n):
    maze.append(list(map(int,str(input("미로의 정보를 입력하세요:")))))