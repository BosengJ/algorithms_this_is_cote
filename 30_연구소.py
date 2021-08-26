# 백준 https://www.acmicpc.net/problem/14502

from collections import deque

# n,m = map(int,input("n,m >"))
# maps = []
# for i in range(n):
#     maps.append(list(map(int,input("maps >"))))

n,m = 4,6
maps = [
    [0, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 2], 
    [1, 1, 1, 0, 0, 2], 
    [0, 0, 0, 0, 0, 2]
    ]

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

cnt_wall = 0
max_zero = 0
for i in range(n):
    for j in range(m):
        if (cnt_wall < 3) and (maps[i][j] == 0):
            maps[i][j] = 1
            cnt_wall += 1
        if cnt_wall == 3:
            
            # 바이러스 퍼뜨리기
            tmp = maps[:]
            virus_maps = virusBFS(tmp, n, m)

            print(maps)
            print(virus_maps)

            # 0 카운트하여 max 값과 비교
            cnt_zero = cntZero(virus_maps)
            if cnt_zero > max_zero:
                max_zero = cnt_zero
            
            # 벽 하나 없애기
            maps[i][j] = 0
            cnt_wall -= 1

print(max_zero)
print(maps)