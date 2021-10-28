fourDirections = [[-1,0], [0,1], [1,0], [0,-1]]  
x,y = 0,0
for direction in fourDirections:
    nx,ny = 0,0
    nx = x + direction[0]
    ny = y + direction[1]
    print(nx,ny)