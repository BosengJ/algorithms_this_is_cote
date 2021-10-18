import sys
from collections import deque

# n = int(sys.stdin.readline())
# maps = []
# for i in range(n):
#     maps.append(list(map(str,sys.stdin.readline().split())))

# n = 5
# maps = [
#     ['X', 'S', 'X', 'X', 'T'], 
#     ['T', 'X', 'S', 'X', 'X'], 
#     ['X', 'X', 'X', 'X', 'X'], 
#     ['X', 'T', 'X', 'X', 'X'], 
#     ['X', 'X', 'T', 'X', 'X']
#     ]

n = 4
maps = [
    ['S', 'S', 'S', 'T'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['T', 'T', 'T', 'X'] 
]

# n = 5
# maps = [
#     ['X', 'S', 'X', 'O', 'T'], 
#     ['T', 'O', 'S', 'X', 'X'], 
#     ['X', 'X', 'O', 'X', 'X'], 
#     ['X', 'T', 'X', 'X', 'X'], 
#     ['X', 'X', 'T', 'X', 'X']
#     ]

# 2차원 배열 복사하는 함수
def copyarray(li):
    array_row = len(li)
    array_column = len(li[0])
    
    copy = []
    for i in range(array_row):
        tmp = []
        for j in range(array_column):
            tmp.append(li[i][j])
        copy.append(tmp)
    return copy

a = copyarray(maps)
print(maps)
print(a)

# BFS 진행시, 상하좌우로 감시하는 함수
def up(x,y,li):
    while x > 0:
        x -= 1
        if li[x][y] == "S":
            li[x][y] = "catch"
        elif li[x][y] == "O":
            break
    return li

def down(x,y,li):
    while x < len(li)-1:
        x += 1
        if li[x][y] == "S":
            li[x][y] = "catch"
        elif li[x][y] == "O":
            break
    return li

def left(x,y,li):
    while y > 0:
        y -= 1
        if li[x][y] == "S":
            li[x][y] = "catch"
        elif li[x][y] == "O":
            break
    return li

def right(x,y,li):
    while y < len(li)-1:
        y += 1
        if li[x][y] == "S":
            li[x][y] = "catch"
        elif li[x][y] == "O":
            break
    return li

# 선생님이 감시하는 BFS 함수
def teacherWatchBFS(li,n):
    q = deque([])
    for i in range(n):
        for j in range(n):
            if li[i][j] == "T":
                q.append([i,j])

    while q:
        x,y = q.popleft()
        up(x,y,li)
        down(x,y,li)
        left(x,y,li)
        right(x,y,li)
        
    return li

# 지도를 확인해서 선생님의 감시를 피했는지 여부를 확인하는 함수
def checkmaps(new_maps):
    answer = ''
    for i in range(len(new_maps)):
        for j in range(len(new_maps)):
            if "catch" not in new_maps[i][j]:
                answer = "YES"
    if len(answer) == 0:
            answer = "NO"
    return answer

# 3개의 장애물을 설치하는 모든 경우의 수
def obstacleDFS(cnt_obs):
    global answer

    if cnt_obs == 3:
        new_maps = teacherWatchBFS(maps,n)
        answer = checkmaps(new_maps)
        return
    
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 'X':
                maps[i][j] = 'O'
                obstacleDFS(cnt_obs+1)

                # obstacleDFS에서 빠져 나오면 원회복
                maps[i][j] = 'X'


# obstacleDFS(0)

# print(answer)
