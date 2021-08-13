# p152 미로 탈출

from collections import deque

n,m = map(int,input("n,m을 공백으로 구분하여 입력하세요:").split())
maps = []
for i in range(n):
    maps.append(list(map(int,input("미로의 정보를 입력하세요:"))))

# n,m = 5,6
# maps = [
#     [1, 0, 1, 0, 1, 0], 
#     [1, 1, 1, 1, 1, 1], 
#     [0, 0, 0, 0, 0, 1], 
#     [1, 1, 1, 1, 1, 1], 
#     [1, 1, 1, 1, 1, 1]
#     ]

def bfs(x,y,li,n,m):
    queue = deque([[x,y]])

    while queue:
        a,b = queue.popleft()

        if (a-1 >= 0) and (li[a-1][b] == 1):       # 위
            li[a-1][b] = li[a][b] + 1
            queue.append([a-1,b])
        
        if (a+1 < n) and (li[a+1][b] == 1):        # 아래
            li[a+1][b] = li[a][b] + 1
            queue.append([a+1,b])
        
        if (b-1 >= 0) and (li[a][b-1] == 1):       # 왼쪽
            li[a][b-1] = li[a][b] + 1
            queue.append([a,b-1])
        
        if (b+1 < m) and (li[a][b+1] == 1):        # 오른쪽
            li[a][b+1] = li[a][b] + 1
            queue.append([a,b+1])

        if (a == n) and (b == m):
            break
    return li

map_step = bfs(0,0,maps,n,m)
answer = map_step[n-1][m-1]
print(answer)

