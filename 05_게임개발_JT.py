
def checkMaps(y, x, maps):
    directions = [[0,1], [0, -1], [1, 0], [-1,0]]
    for dir in directions:
        changed_y = y + dir[0]
        changed_x = x + dir[1]
        if maps[changed_y][changed_x] == 0:
            return False
    return True

def moveAvata(y,x, move):
    return y + move[0], x + move[1]

def changeDirection(dir):
    dir = dir - 1
    if dir == -1:
        dir = 3
    return dir

# get input
N, M = map(int, input().split(' '))
y, x, dir = map(int, input().split(' '))
maps = []
move_back = {0:[1,0], 1:[0, -1], 2:[-1, 0], 3: [0,1]}
move_left = {0:[0,-1], 1:[-1, 0], 2:[0, 1], 3: [1,0]}
for i in range(M):  
    maps.append(list(map(int, input().split(' '))))


stop_move = False
move_cnt = 1
maps[y][x]=2
while(stop_move == False):
    if checkMaps(y, x, maps):
        changed_y,changed_x = moveAvata(y,x, move_back[dir])
        if maps[changed_y][changed_x] == 1:
            stop_move= True
        else:
            y, x = changed_y,changed_x
        continue
    changed_y, changed_x = moveAvata(y, x, move_left[dir])
    if maps[changed_y][changed_x] == 0:
        y, x = changed_y, changed_x
        maps[changed_y][changed_x] = 2
        move_cnt += 1
    dir =changeDirection(dir)

print(move_cnt)