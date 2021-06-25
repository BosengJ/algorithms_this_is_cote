# 현재 위치를 기준으로 사방에 육지가 있는지 없는지 판별
def searchLand(map,location):
    i,j = location
    if i-1 >= 0:
        n = map[i-1][j]
    if j+1 < len(map[0]):
        e = map[i][j+1]
    if i+1 < len(map):
        s = map[i+1][j]
    if j-1 >= 0:
        w = map[i][j-1]
    if n == 0 or e == 0 or s==0 or w==0:
        return True
    else: 
        return False


# def searchLeftValue(d,x,y):
#     if d == 0:                  # 북
#         x,y = x,y
#     if d == 1:                  # 동
#     if d == 2:                  # 남
#     if d == 3:                  # 서
#     return left_val

def solution(map,location):
    current_location = location[:2]
    d = location[-1]
    y,x = current_location
    map[y][x] = 2               # 방문한 곳은 2로 표시해준다. 시작 위치도 방문했기 때문에 2로 바꿔줬다.
    a = searchLand(map,location)
    print(a)
    

    # while map[y][x] != 1:       # 위치가 육지를 벗어나는 순간 멈춘다.
    #     left_val = searchLeftValue(d,x,y)
    #     if left_val == 0:


    answer = []
    return answer

map = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
location = [1,1,0]
a = solution(map,location)
print(a)