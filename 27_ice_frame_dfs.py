n,m = map(int,input("n,m을 공백을 구분으로 입력하세요:").split())
ice_frame = []
for i in range(n):
    ice_frame.append(list(map(int,str(input("얼음 틀 형태를 입력하세요:")))))

# n,m = 4, 5
# ice_frame = [
#     [0, 0, 1, 1, 0], 
#     [0, 0, 0, 1, 1], 
#     [1, 1, 1, 1, 1], 
#     [0, 0, 0, 0, 0]
#     ]

def check0_turn1(li,x,y):
    if (x-1 >= 0) and (li[x-1][y] == 0): # 위쪽 확인
        li[x-1][y] = 1
        li = check0_turn1(li,x-1,y)

    if (y-1 >= 0) and (li[x][y-1] == 0): # 왼쪽 확인
        li[x][y-1] = 1
        li = check0_turn1(li,x,y-1)

    if (y+1 < m) and (li[x][y+1] == 0): # 오른쪽 확인
        li[x][y+1] = 1
        li = check0_turn1(li,x,y+1)

    if (x+1 < n) and (li[x+1][y] == 0): # 아래쪽 확인
        li[x+1][y] = 1
        li = check0_turn1(li,x+1,y)
    return li

icecream = 0
for i in range(n):
    for j in range(m):
        if ice_frame[i][j] == 0:
            ice_frame[i][j] = 1
            ice_frame = check0_turn1(ice_frame,i,j)
            icecream += 1
print(icecream)