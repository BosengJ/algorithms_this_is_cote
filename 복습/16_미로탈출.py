# p152 미로 탈출

from collections import deque

# n,m = map(int,input("n,m을 공백으로 구분하여 입력하세요:").split())
# maps = []
# for i in range(n):
#     maps.append(list(map(int,input("미로의 정보를 입력하세요:"))))

n,m = 5,6
maps = [
    [1, 0, 1, 0, 1, 0], 
    [1, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 1], 
    [1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1]
    ]