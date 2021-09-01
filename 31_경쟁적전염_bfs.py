from collections import deque
import sys

n,k = map(int,sys.stdin.readline().split())
tube = []
for i in range(n):
    tube.append(list(map(int,sys.stdin.readline().split())))
s,x,y = map(int,sys.stdin.readline().split())

# n,k = 3,3
# tube = [[1, 0, 2], [0, 0, 0], [3, 0, 0]]
# s,x,y = 1,2,2

# n,k = 3,3
# tube = [[0, 2, 1], [0, 0, 0], [3, 0, 0]]
# s,x,y = 1,2,2

# 초기값 설정
q = deque([])
for virus in range(1,k+1):
    for i in range(n):
        for j in range(n):
            if tube[i][j] == virus:
                q.append([0,virus,i,j])

dx = [0,0,-1,1]
dy = [-1,1,0,0]

while q:
    t, v, vx, vy = q.popleft()   # t(경과시간), v(바이러스종류), vx(행 위치값), vy(열 위치값)
    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]
        if (t < s) and (nx >= 0) and (nx < n) and (ny >= 0) and (ny < n):
            if tube[nx][ny] == 0:
                q.append([t+1, v, nx, ny])
                tube[nx][ny] = v

answer = tube[x-1][y-1]
print(answer)
