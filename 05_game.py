# 현재 위치를 기준으로 사방에 어떤 값이 있는지 확인하는 함수 4개

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

# 바라보는 방향을 기준으로, 한칸 이동했을 때의 위치를 확인하는 함수 4개

def find_northIdx(current_location):        # 북쪽으로 이동했을 때의 인덱스
    i,j = current_location
    i -= 1
    return [i,j]

def find_eastIdx(current_location):         # 동쪽으로 이동했을 때의 인덱스
    i,j = current_location
    j += 1
    return [i,j]

def find_southIdx(current_location):        # 남쪽으로 이동했을 때의 인덱스
    i,j = current_location
    i += 1
    return [i,j]

def find_westIdx(current_location):         # 서쪽으로 이동했을 때의 인덱스
    i,j = current_location
    j -= 1
    return [i,j]






def solution(map,location):
    # 초기값 출력
    print('start!')
    print('map:',map)

    current_location = location[:2]
    d = location[-1]
    y,x = current_location
    map[y][x] = 2            # 방문한 곳은 2로 표시해준다 (시작 위치도 방문했기 때문에 2로 바꿔줬다)
    print('map:',map)
    print('current_location:',current_location)
    print('d:',d)

    while True:
        
        # 현재 위치를 기준으로 네 방향의 값을 확인한다
        n_val = find_northVal(map,current_location)
        e_val = find_eastVal(map,current_location)
        s_val = find_southVal(map,current_location)
        w_val = find_westVal(map,current_location)
        
        '''현재 위치를 기준으로 네 방향의 값을 확인하여, 

        1) 한 방향이라도 가보지 않은 육지가 있는 경우,
            왼쪽값을 확인해서,
            a) 왼쪽값이 육지이면서 아직 가보지 않은 경우
            b) 왼쪽값이 육지가 아닌 경우로 나누어 진행한다

        2) 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 경우'''

        # 1) 네 방향 하나라도 육지가 있을 경우
        if (n_val == 0) or (e_val == 0) or (s_val == 0) or (w_val == 0): 
            print('one of 4 direction, there is land')

            # 현재 바라보는 방향을 기준으로 왼쪽값(left_val)을 확인해본다
            if d == 0:               # 북쪽을 바라보고 있다면 왼쪽인 서쪽 값을 구한다
                left_val = find_westVal(map,current_location)
            if d == 1:               # 동쪽을 바라보고 있다면 왼쪽인 북쪽 값을 구한다
                left_val = find_northVal(map,current_location)
            if d == 2:               # 남쪽을 바라보고 있다면 왼쪽인 동쪽 값을 구한다
                left_val = find_eastVal(map,current_location)
            if d == 3:               # 서쪽을 바라보고 있다면 왼쪽인 남쪽 값을 구한다
                left_val = find_southVal(map,current_location)
            print('left_val:',left_val)

            '''확인한 왼쪽값을 가지고
            a) 왼쪽값이 육지이면서 아직 가보지 않은 경우
            b) 왼쪽값이 육지가 아닌 경우로 나누어 진행한다
            '''

            # a) 왼쪽값(left_val)이 육지이면서 아직 가보지 않은 경우
            if left_val == 0:
                # print('left! there is land')
                # 바라보는 방향을 왼쪽으로 이동시켜 준 다음,
                d -= 1
                if d < 0:
                    d = 3
                # 바뀐 바라보는 방향으로 현재 위치를 한 칸 이동시켜준다
                if d == 0:
                    current_location = find_northIdx(current_location)
                if d == 1:
                    current_location = find_eastIdx(current_location)
                if d == 2:
                    current_location = find_southIdx(current_location)
                if d == 3:
                    current_location = find_westIdx(current_location)
                print('d:',d)
                print('current_location:',current_location)

                # 이동한 곳의 값을 2로 바꿔준다.
                y,x = current_location
                map[y][x] = 2  
                print('map:',map)

            # b) 왼쪽값(left_val)이 육지가 아닌 경우, 바라보는 방향을 왼쪽으로 회전시켜준다
            else:
                d -= 1
                if d < 0:
                    d = 3
                print('left! no land')
                print('d:',d)

        # 2) 네 방향 모두 이미 가본 칸이거나 바다로 되어있는 경우, 방향을 유지한 채 뒤로 한 칸 이동한다
        else:
            print('4 direction, no land')
            if d == 0:
                current_location = find_southIdx(current_location)
            if d == 1:
                current_location = find_westIdx(current_location)
            if d == 2:
                current_location = find_northIdx(current_location)
            if d == 3:
                current_location = find_eastIdx(current_location)
            print(current_location)

            # 이동한 곳의 값이 가보지 않은 육지일 경우 2로 바꿔줘고, 바다일 경우 게임을 중단한다
            y,x = current_location
            current_val = map[y][x]
            if current_val == 1:
                print('current_location:',current_location,'current_val:',current_val)
                print('the game is over!')
                break
        print(map)
    print('fianl map:',map)

    # 방문한 육지의 개수를 카운트 한다
    cnt = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 2:
                cnt += 1
    return cnt

# test case

# map = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
# location = [1,1,0]
# 답 3

# 무한루프 - > 수정완료! 테스트케이스 통과!
map = [[1,1,1,1,1],[1,0,1,0,1],[1,0,1,0,1],
[1,0,0,0,1],[1,0,1,0,1],[1,0,1,0,1],[1,1,1,1,1]]
location = [3,2,1]

# 통과
# map = [[1,1,1,1],[1,0,0,1],[1,0,1,0],[1,1,1,1]]
# location = [1,1,0]
# 답 3

# 통과
# map = [[1,1,1,1],[1,0,1,1],[1,0,0,1],[1,0,1,1],[1,1,1,1]]
# location = [1,1,0]
# 답 4

# 통과
# map = [[1,1,1,1,1,1],[1,0,0,1,1,1],[1,1,0,0,1,1],[1,1,1,0,0,1],[1,1,1,1,1,1]]
# location = [2,2,0]
# 답 4

a = solution(map,location)
print(a)

