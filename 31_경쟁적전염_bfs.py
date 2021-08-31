from collections import deque

# n,k = map(int,input().split())
# tube = []
# for i in range(n):
#     tube.append(list(map(int,input().split())))
# s,x,y = map(int,input().split())

n,k = 3,3
tube = [[1, 0, 2], [0, 0, 0], [3, 0, 0]]
s,x,y = 1,2,2


q = deque([])
for virus in range(1,k+1):
    for i in range(n):
        for j in range(n):
            if tube[i][j] == virus:
                q.append([virus,i,j])

dx = [0,0,-1,1]
dy = [-1,1,0,0]

while q:
    v, vx, vy = q.popleft()
    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]
        if (nx >= 0) and (nx < n) and (ny >= 0) and (ny < n):
            if tube[nx][ny] == 0:
                q.append([v,nx,ny])
                tube[nx][ny] = v

answer = tube[x-1][y-1]
print(tube)
print(answer)
