import sys
from collections import deque

# n = int(sys.stdin.readline())
# maps = []
# for i in range(n):
#     maps.append(list(map(str,sys.stdin.readline().split())))

n = 5
maps = [
    ['X', 'S', 'X', 'X', 'T'], 
    ['T', 'X', 'S', 'X', 'X'], 
    ['X', 'X', 'X', 'X', 'X'], 
    ['X', 'T', 'X', 'X', 'X'], 
    ['X', 'X', 'T', 'X', 'X']
    ]

# n = 5
# maps = [
#     ['X', 'S', 'X', 'O', 'T'], 
#     ['T', 'O', 'S', 'X', 'X'], 
#     ['X', 'X', 'O', 'X', 'X'], 
#     ['X', 'T', 'X', 'X', 'X'], 
#     ['X', 'X', 'T', 'X', 'X']
#     ]

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

        if (up_ == False) or (down_ == False) or (left_ == False) or (right_ == False):
            print(1)
            return "NO"

    return "YES"

a = teacherWatchBFS(maps,n)
print(a)
