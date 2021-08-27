# 백준 https://www.acmicpc.net/problem/14502

from collections import deque
import copy

n,m = map(int,input("n,m >").split())
maps = []
for i in range(n):
    maps.append(list(map(int,input("maps >").split())))

# n,m = 4,6
# maps = [
#     [0, 0, 0, 0, 0, 0], 
#     [1, 0, 0, 0, 0, 2], 
#     [1, 1, 1, 0, 0, 2], 
#     [0, 0, 0, 0, 0, 2]
#     ]

max_zero = 0

def virusBFS(li, n, m):
    q = deque([])
    for i in range(n):
        for j in range(m):
            if li[i][j] == 2:
                q.append([i,j])
                while q:
                    x,y = q.popleft()
                    # 위
                    if (x-1 >= 0) and (li[x-1][y] == 0):
                        q.append([x-1, y])
                        li[x-1][y] = 2
                    # 아래
                    if (x+1 < n) and (li[x+1][y] == 0):
                        q.append([x+1, y])
                        li[x+1][y] = 2
                    # 왼
                    if (y-1 >= 0) and (li[x][y-1] == 0):
                        q.append([x, y-1])
                        li[x][y-1] = 2
                    # 오른
                    if (y+1 < m) and (li[x][y+1] == 0):
                        q.append([x, y+1])
                        li[x][y+1] = 2
    return li   

def cntZero(li):
    c = 0
    for i in range(len(li)):
        for j in range(len(li[i])):
            if li[i][j] == 0:
                c += 1
    return c

def wallDFS(cnt_wall, x, y):
    global max_zero

    # 벽 3개 완성됐을 때,
    if cnt_wall == 3:
        # 바이러스 퍼뜨리기
        tmp =  copy.deepcopy(maps)
        virus_maps = virusBFS(tmp, n, m)

        # 0 카운트하여 max 값과 비교
        cnt_zero = cntZero(virus_maps)
        max_zero = max(max_zero, cnt_zero)
        return 
    
    for i in range(x,n):
        if i == x:
            k = y
        else:
            k = 0
        for j in range(k,m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                cnt_wall += 1
                wallDFS(cnt_wall, x, y)

                # wallDFS에서 빠져 나오면 벽 하나 없애기
                maps[i][j] = 0
                cnt_wall -= 1

wallDFS(0,0,0)
print(max_zero)