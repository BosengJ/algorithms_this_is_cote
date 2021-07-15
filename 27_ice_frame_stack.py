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

icecream = 0
for i in range(n):
    for j in range(m):
        if ice_frame[i][j] == 0:
            ice_frame = check0_turn1(ice_frame,i,j,m,n)
            icecream += 1
print(icecream)