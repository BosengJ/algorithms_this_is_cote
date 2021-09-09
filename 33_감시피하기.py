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

n = 5
maps = [
    ['X', 'S', 'X', 'O', 'T'], 
    ['T', 'O', 'S', 'X', 'X'], 
    ['X', 'X', 'O', 'X', 'X'], 
    ['X', 'T', 'X', 'X', 'X'], 
    ['X', 'X', 'T', 'X', 'X']
    ]

# BFS 진행시, 상하좌우로 감시하는 함수
def up(x,y,li):
    while x > 0:
        x -= 1
        if li[x][y] == "S":
            return "False"
        elif li[x][y] == "O":
            break
    return "True"

def down(x,y,li):
    while x < len(li)-1:
        x += 1
        if li[x][y] == "S":
            return "False"
        elif li[x][y] == "O":
            break
    return "True"

def left(x,y,li):
    while y > 0:
        y -= 1
        if li[x][y] == "S":
            return "False"
        elif li[x][y] == "O":
            break
    return "True"

def right(x,y,li):
    while y < len(li)-1:
        y += 1
        if li[x][y] == "S":
            return "False"
        elif li[x][y] == "O":
            break
    return "True"

# 선생님이 감시하는 BFS 함수
def teacherWatchBFS(li,n):
    q = deque([])
    for i in range(n):
        for j in range(n):
            if li[i][j] == "T":
                q.append([i,j])
    while q:
        x,y = q.popleft()
        up_ = up(x,y,li)
        down_ = down(x,y,li)
        left_ = left(x,y,li)
        right_ = right(x,y,li)
    
    print(up_), print(down_), print(left_), print(right_)
    if (up_ == True) and (down_ == True) and (left_ == True) and (right_ == True):
        return "YES"
    else:
        return "NO"

a = teacherWatchBFS(maps,n)
print(a)
