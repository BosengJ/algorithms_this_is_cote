# input
n,m = map(int,input("맵의 세로 크기 n과 가로 크기 m을 공백으로 구분하여 입력하세요").split())
x,y,d = map(int,input("게임 캐릭터가 있는 칸의 좌표 x,y와 바라보는 방향 d를 공백으로 구분하여 입력하세요 >").split())
maps = []
for i in range(n):
    maps.append(list(map(int,input("n개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 입력하세요 >").split())))

# test case
n,m = 4,4
x,y,d = 1,1,0
maps = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]