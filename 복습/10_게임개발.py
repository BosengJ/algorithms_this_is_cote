# p118 게임 개발

# n,m = map(int,input("맵의 세로크기 n과 가로 크기 m을 공백으로 구분하여 입력하세요:").split())
# a,b,d = map(int,input("좌표 A, B 와 바라보는 방향 d를 공백으로 구분하여 입력하세요:").split())
# location = [a,b]
# map_li = []
# for i in range(n):
#     map_li.append(list(map(int,input("맵 정보를 입력하세요:").split())))

n,m = 4,4
location = [1,1]
d = 1
map_li = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]