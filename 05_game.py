# 현재 위치를 기준으로 사방에 어떤 값이 있는지 판별하는 함수 4개
def find_northVal(map,location):    # 북쪽의 값
    i,j = location
    if i-1 >= 0:
        n_val = map[i-1][j]     
    else:
        n_val = 'none'
    return n_val

def find_eastVal(map,location):    # 동쪽의 값
    i,j = location
    if j+1 < len(map[0]):
        e_val = map[i][j+1]     
    else:
        e_val = 'none'
    return e_val
    
def find_southVal(map,location):   # 남쪽의 값
    i,j = location
    if i+1 < len(map):
        s_val = map[i+1][j]
    else:
        s_val = 'none'  
    return s_val

def find_southVal(map,location):   # 서쪽의 값
    i,j = location
    if j-1 >= 0:
        w_val = map[i][j-1]     
    else: 
        w_val = 'none'
    return w_val

# 현재 위치를 기준으로 사방에 육지가 있는지 없는지 판별하는 함수
def searchLand(map,location):
    i,j = location
    if i-1 >= 0:
        n = map[i-1][j]     # 북쪽의 값
    if j+1 < len(map[0]):
        e = map[i][j+1]     # 동쪽의 값
    if i+1 < len(map):
        s = map[i+1][j]     # 남쪽의 값
    if j-1 >= 0:
        w = map[i][j-1]     # 서쪽의 값
    if n == 0 or e == 0 or s==0 or w==0:
        return True
    else: 
        return False

# 현재 바라보는 방향을 기준으로 왼쪽에 무슨 값이 있는지 알아내는 함수
def searchLeftValue(location,d,map):
    i,j = location
    if (j-1 >= 0) and (d == 0):              # 북
        left_val = map[i][j-1]
    elif (i-1 >= 0) and (d == 1):            # 동
        left_val = map[i-1][j]
    elif (j+1 < len(map[0])) and (d == 2):   # 남
        left_val = map[i][j+1]
    elif (i+1 < len(map)) and (d == 3):      # 서
        left_val = map[i+1][j]
    else:
        left_val = 'none'
    return left_val

def solution(map,location):
    current_location = location[:2]
    d = location[-1]
    y,x = current_location
    map[y][x] = 2        # 방문한 곳은 2로 표시해준다. 시작 위치도 방문했기 때문에 2로 바꿔줬다.
    
    # 네 방향 하나라도 육지가 있을 경우
    if searchLand(map,current_location) == True:
        left_val = searchLeftValue(current_location,d,map)
        print(map)
        print(current_location)
        print(left_val)

        if left_val == '0': # 육지가 존재한다면
            d -= 1          # 방향을 왼쪽으로 이동한 다음
            if d < 0:
                d = 3       # 단, 방향이 북에서 서로 바뀔 때는 d 값이 -1 되기 때문에 3으로 다시 맞춰준다.
           
            # 이 부분이 반복되므로 위의 함수 모두 다 기능 하나로 정리해준다.
            if d == 0:
            elif d == 1:
            elif d == 2:
            elif d == 3:

            print('aa')
        else:
            print('bb')
    
    # 네 방향 모두 이미 가본 칸이거나 바다로 되어있는 경우
    else:
        print('bb')
    

    # while map[y][x] != 1:       # 위치가 육지를 벗어나는 순간 멈춘다.
    #     left_val = searchLeftValue(d,x,y)
    #     if left_val == 0:


    answer = []
    return answer

map = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
location = [1,1,0]
a = solution(map,location)
print(a)