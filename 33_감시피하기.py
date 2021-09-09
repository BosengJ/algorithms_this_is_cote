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

