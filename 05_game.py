# 현재 위치를 기준으로 사방에 어떤 값이 있는지 판별하는 함수 4개

def find_northVal(map,current_location):    # 북쪽의 값
    i,j = current_location
    if i-1 >= 0:
        n_val = map[i-1][j]     
    else:
        n_val = 'none'
    return n_val

def find_eastVal(map,current_location):     # 동쪽의 값
    i,j = current_location
    if j+1 < len(map[0]):
        e_val = map[i][j+1]     
    else:
        e_val = 'none'
    return e_val
    
def find_southVal(map,current_location):    # 남쪽의 값
    i,j = current_location
    if i+1 < len(map):
        s_val = map[i+1][j]
    else:
        s_val = 'none'  
    return s_val

def find_westVal(map,current_location):     # 서쪽의 값
    i,j = current_location
    if j-1 >= 0:
        w_val = map[i][j-1]     
    else: 
        w_val = 'none'
    return w_val

def solution(map,location):
    current_location = location[:2]
    d = location[-1]
    y,x = current_location
    map[y][x] = 2                           # 방문한 곳은 2로 표시해준다 (시작 위치도 방문했기 때문에 2로 바꿔줬다)
    
    
    # while 처리 해준다 (조건이 끝날 때 까지 무한 반복 해야한다)
    # 현재 위치를 기준으로 사방의 값을 확인한다
    n_val = find_northVal(map,current_location)
    e_val = find_eastVal(map,current_location)
    s_val = find_southVal(map,current_location)
    w_val = find_westVal(map,current_location)
    
    # 네 방향 하나라도 육지가 있을 경우
    if (n_val == 0) or (e_val == 0) or (s_val == 0) or (w_val == 0): 
        print(map)
        print('current_location:',current_location)
        print('d:',d)
        print('there is land')

        # 현재 바라보는 방향을 기준으로 왼쪽 값을 확인해본다
        if d == 0:               # 북쪽을 바라보고 있다면 왼쪽인 서쪽 값을 구한다
            left_val = find_westVal(map,current_location)
        if d == 1:               # 동쪽을 바라보고 있다면 왼쪽인 북쪽 값을 구한다
            left_val = find_eastVal(map,current_location)
        if d == 2:               # 남쪽을 바라보고 있다면 왼쪽인 동쪽 값을 구한다
            left_val = find_eastVal(map,current_location)
        if d == 3:               # 서쪽을 바라보고 있다면 왼쪽인 남쪽 값을 구한다
            left_val = find_southVal(map,current_location)
        print(left_val)

        # 왼쪽 값이 육지이면서 아직 가보지 않은 경우
        if left_val == 0:
            print('left, there is land')
            
        # 왼쪽 값이 육지가 아닌 경우
        else:
            d -= 1
            if d < 0:
                d = 3
            print('left, no land')
            print('d:',d)

    # 네 방향 모두 이미 가본 칸이거나 바다로 되어있는 경우
    else:
        print('no land')

    return []

map = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
location = [1,1,0]
a = solution(map,location)
print(a)