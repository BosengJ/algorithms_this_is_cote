# p149 음료수 얼려 먹기

from collections import deque

# n,m = map(int,input("공백을 기준으로 n,m을 입력하세요:").split())
# icebox = []
# for i in range(n):
#     icebox.append(list(map(int,input("얼음 틀의 형태를 입력하세요:"))))
n,m = 4,5
icebox = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

def bfs(x,y,li,n,m):
    queue = deque([[x,y]])
    li[x][y] = 1

    while queue:
        a,b = queue.popleft()

        if (a-1 >= 0) and (li[a-1][b] == 0):    # 위
            queue.append([a-1,b])
            li[a-1][b] = 1
        if (a+1 < n) and (li[a+1][b] == 0):     # 아래
            queue.append([a+1,b])
            li[a+1][b] = 1
        if (b-1 >= 0) and (li[a][b-1] == 0):    # 왼쪽
            queue.append([a,b-1])
            li[a][b-1] = 1
        if (b+1 < m) and (li[a][b+1] == 0):     # 오른쪽
            queue.append([a,b+1])
            li[a][b+1] = 1
    return li

icecream = 0
for i in range(n):
    for j in range(m):
        if icebox[i][j] == 0:
            icebox = bfs(i,j,icebox,n,m)
            icecream += 1
print(icecream)
