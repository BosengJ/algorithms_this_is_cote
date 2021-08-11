# p118 게임 개발
# test case

# map = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
# location = [1,1,0]
# 답 3

# 무한루프 - > 수정완료! 테스트케이스 통과!
# map = [[1,1,1,1,1],[1,0,1,0,1],[1,0,1,0,1],
# [1,0,0,0,1],[1,0,1,0,1],[1,0,1,0,1],[1,1,1,1,1]]
# location = [3,2,1]

# 통과
# map = [[1,1,1,1],[1,0,0,1],[1,0,1,0],[1,1,1,1]]
# location = [1,1,0]
# 답 3

# 통과
# map = [[1,1,1,1],[1,0,1,1],[1,0,0,1],[1,0,1,1],[1,1,1,1]]
# location = [1,1,0]
# 답 4

# 통과
# map = [[1,1,1,1,1,1],[1,0,0,1,1,1],[1,1,0,0,1,1],[1,1,1,0,0,1],[1,1,1,1,1,1]]
# location = [2,2,0]
# 답 4

n,m = map(int,input("맵의 세로크기 n과 가로 크기 m을 공백으로 구분하여 입력하세요:").split())
x,y,d = map(int,input("좌표 A, B 와 바라보는 방향 d를 공백으로 구분하여 입력하세요:").split())
maps = []
for i in range(n):
    maps.append(list(map(int,input("맵 정보를 입력하세요:").split())))

# n,m = 4,4
# x,y = 1,1
# d = 1
# maps = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]

# 인덱스0:북으로 이동, 1:동으로 이동, 2:남으로 이동, 3:서로 이동
move = [[-1,0],[0,1],[1,0],[0,-1]] 

# 왼쪽으로 회전 후 바라보는 방향 구하기
def turn_left(direction):
    direction -= 1
    if direction < 0:
        direction = 3
    return direction

# 초기값
maps[x][y] = 1
cnt = 1
turn = 0

while True:
    d = turn_left(d)
    nx = x + move[d][0]
    ny = y + move[d][1]

    if maps[nx][ny] == 0:
        maps[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn = 0
    else:
        turn += 1
    
    if turn == 4:
        nx = x - move[d][0]
        ny = y - move[d][1]
        if maps[nx][ny] == 0:
            x = nx
            y = ny
            turn = 0
        else:
            break
print(cnt)

