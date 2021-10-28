from collections import deque
import copy

# input
# n,m = map(int,input("얼음틀의 세로 길이 n과 가로 길이 m을 공백을 기준으로 입력하세요 >").split())
# frame = []
# for i in range(n):
#     frame.append(list(map(int,input("얼음 틀의 형태를 구멍(0), 그렇지 않은 부분(1)로 입력하세요 >"))))

n,m = 4,5
mold = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

# bfs 방법으로 구멍이 뚫려 있는 부분(0)을 확인한다
def checkZero(p,q,li):
    return li

# for문을 사용하여 얼음 틀의 구멍이 뚫려 있는 부분(0)을 확인해 주고 bfs를 통해 생성되는 아이스크림 개수를 구한다

# 원본 보존을 위해 얼음 틀 리스트는 복사해서 사용한다
n_mold = copy.deepcopy(mold)

iceCream = 0
for i in range(n):
    for j in range(m):
        modified_mold = checkZero(i,j,n_mold)
        iceCream += 1
print(iceCream)
