def solution(map,location):
    current_location = location[:2]
    d = location[-1]
    y,x = current_location
    map[y][x] = 2               # 방문한 곳은 2로 표시해준다. 시작 위치도 방문했기 때문에 2로 바꿔줬다.
    
    while map[y][x] != 1: # 위치가 육지를 벗어나는 순간 멈춘다.
        if left == 0:
            d -= 1
            if d < 0:
                d = 3
            y,x = 



    answer = []
    return answer

map = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
location = [1,1,0]
a = solution(map,location)
print(a)