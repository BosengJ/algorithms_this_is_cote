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

b = [
    [0,0,0,0,0,1],
    [1,0,0,0,1,2],
    [1,1,1,1,0,2],
    [0,0,0,0,0,2]
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

cnt = 0
max = 0
for i in range(n):
    for j in range(m):
        if (cnt < 3) and (maps[i][j] == 0):
            maps[i][j] = 1
            cnt += 1
        if cnt == 3:
            # 바이러스 -> 0 cnt -> max와 비교
            
            maps[i][j] = 0
            cnt -= 1
print(maps)
