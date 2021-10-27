from collections import deque
import copy

# test case

# maps = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
# x,y,d = 1,1,0
# 답 3

# maps = [[1,1,1,1,1],[1,0,1,0,1],[1,0,1,0,1],
# [1,0,0,0,1],[1,0,1,0,1],[1,0,1,0,1],[1,1,1,1,1]]
# x,y,d = 3,2,1

# !!!
# maps = [[1,1,1,1],[1,0,0,1],[1,0,1,0],[1,1,1,1]]
# x,y,d = 1,1,0
# 답 3

# !!!
# maps = [[1,1,1,1],[1,0,1,1],[1,0,0,1],[1,0,1,1],[1,1,1,1]]
# x,y,d = 1,1,0
# 답 4

# 통과
# maps = [[1,1,1,1,1,1],[1,0,0,1,1,1],[1,1,0,0,1,1],[1,1,1,0,0,1],[1,1,1,1,1,1]]
# x,y,d = 2,2,0
# 답 4

# input
# n,m = map(int,input("맵의 세로 크기 n과 가로 크기 m을 공백으로 구분하여 입력하세요").split())
# x,y,d = map(int,input("게임 캐릭터가 있는 칸의 좌표 x,y와 바라보는 방향 d를 공백으로 구분하여 입력하세요 >").split())
# maps = []
# for i in range(n):
#     maps.append(list(map(int,input("n개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 입력하세요 >").split())))

# 뒤로 물러나는 함수
def backStep(li,x,y):
    north = li[x-1][y]
    east = li[x][y+1]
    south = li[x+1][y]
    west = li[x][y-1]
    if (north != 0) and (east != 0) and (south != 0) and (west != 0):
        return True
    return False

# 다음 스텝을 어디로 갈지 정해주는 함수
def nextStep(li,x,y,z):
    move_dict = {0:[0,-1], 1:[-1,0], 2:[0,1], 3:[1,0]}  # 바라보는 방향을 기준으로 왼쪽 좌표가 무엇인지 알아볼 때 +/- 해줘야 하는 값
    while True:
        n_move = move_dict[z]
        nx = x + n_move[0]
        ny = y + n_move[1]
        z -= 1
        if z < 0:
            z = 3
        if li[nx][ny] == 0:
            n_step = [nx,ny,z]
            break
    return n_step

# bfs
def gameBFS(p,q,r,li):
    n_li = copy.deepcopy(li)      # 기존의 맵을 복사해서 새로운 맵을 만들어준다
    queue = deque([[p,q,r]])          # 초기 위치와 바라보는 방향을 q에 넣는다   
    n_li[p][q] = 2                # 초기값은 방문한 곳이기 때문에 element를 변경해준다
    
    while queue:
        i,j,k = queue.popleft()
        if backStep(n_li,i,j) == True:  # 뒤로 물러나야할 경우를 따져본다
            back_move_dict = {0:[0,-1], 1:[-1,0], 2:[0,1], 3:[1,0]}
            moving = back_move_dict[k]
            n_i = i + moving[0]
            n_j = j + moving[1]
            if li[n_i][n_j] == 2:       # 가본 곳으로 방향을 유지한 채 물러나고, 뒤가 바다(1)라면 q에 더이상 추가하지 않는다
                queue.append([n_i, n_j, k])
        else:
            n_step = nextStep(n_li,i,j,k)   # 다음번 이동할 좌표와 방향을 뽑아낸다
            queue.append(n_step)
            n_li[n_step[0]][n_step[1]] = 2
    return n_li

# 방문한 칸의 개수를 세는 함수
def checkVisited(li):
    cnt = 0
    for i in range(len(li)):
        for j in range(len(li[i])):
            if li[i][j] == 2:
                cnt += 1
    return cnt

n_map = gameBFS(x,y,d,maps)
answer = checkVisited(n_map)

print(answer)