from collections import deque
import copy

# input
# n,m = map(int,input("맵의 세로 크기 n과 가로 크기 m을 공백으로 구분하여 입력하세요").split())
# x,y,d = map(int,input("게임 캐릭터가 있는 칸의 좌표 x,y와 바라보는 방향 d를 공백으로 구분하여 입력하세요 >").split())
# maps = []
# for i in range(n):
#     maps.append(list(map(int,input("n개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 입력하세요 >").split())))

# test case
n,m = 4,4
x,y,d = 1,1,0
maps = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]

# bfs
def gameBFS(p,q,r,li):
    n_li = copy.deepcopy(li)    # 기존의 맵을 복사해서 새로운 맵을 만들어준다
    q = deque([[p,q,r]])          # 초기 위치와 바라보는 방향을 q에 넣는다   
    n_li[p][q] = 2              # 초기값은 방문한 곳이기 때문에 element를 변경해준다
    
    while q:
        i,j,k = q.popleft()

    return n_li

# 방문한 칸의 개수를 세는 함수
def checkVisited(li):
    cnt = 0
    for i in range(len(li)):
        for j in range(len(li[i])):
            if li[i][j] == 2:
                cnt += 1
    return cnt