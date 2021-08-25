# 백준 https://www.acmicpc.net/problem/14502

# n,m = map(int,input("n,m >"))
# maps = []
# for i in range(n):
#     maps.append(list(map(int,input("maps >"))))

n,m = 4,6
maps = [
    [0, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 2], 
    [1, 1, 1, 0, 0, 2], 
    [0, 0, 0, 0, 0, 2]
    ]

cnt = 0
for i in range(n):
    for j in range(m):
        if (cnt < 3) and (maps[i][j] == 0):
            maps[i][j] = 1
            cnt += 1
        if cnt == 3:
            # 바이러스 -> 0 cnt -> max와 비교
            maps[i][j] = 0
            cnt -= 1