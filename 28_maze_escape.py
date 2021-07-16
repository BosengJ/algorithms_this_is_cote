from collections import deque

# n,m = map(int, input("n,m을 공백을 구분으로 입력하세요:").split())
# maze = []
# for i in range(n):
#     maze.append(list(map(int,str(input("미로의 정보를 입력하세요:")))))


n,m = 5,6
maze = [
    [1, 0, 1, 0, 1, 0], 
    [1, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 1], 
    [1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1]
    ]



# 초기값 설정
queue = deque([[0,0]])
maze[0][0] = 0
visited = 1
print(maze)

for i in range(n):
    for j in range(m):
        while queue:
            print(maze)
            p,q = queue.popleft()

            if (p == n-1) and (q == m-1):   # 출구 도착시 종료
                visited -= len(queue)
                break

            if (p-1 >= 0) and (maze[p-1][q] == 1):  # 위쪽 확인
                queue.append([p-1,q])
                maze[p-1][q] = 0
                visited += 1

            if (q-1 >= 0) and (maze[p][q-1] == 1):  # 왼쪽 확인
                queue.append([p,q-1])
                maze[p][q-1] = 0
                visited += 1

            if (q+1 < m) and (maze[p][q+1] == 1):  # 오른쪽 확인
                queue.append([p,q+1])
                maze[p][q+1] = 0
                visited += 1

            if (p+1 < n) and (maze[p+1][q] == 1):  # 아래쪽 확인
                queue.append([p+1,q])
                maze[p+1][q] = 0
                visited += 1

            else:
                visited -= 1
print(visited)