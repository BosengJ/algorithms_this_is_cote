# input
location = input("현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열을 입력하세요 >")

# 행렬을 수치화 해서 각각의 변수에 저장해주는 함수
def currentLocation(str):
    row = int(str[1])
    column = int(ord(str[0])) - int(ord('a')) + 1
    return row, column

# 8가지 L자 형태 움직임 함수
def moveKnight(p,q):
    moves = [[-1,2],[1,2],[-1,-2],[1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
    cnt = 0
    for move in moves:
        np = p + move[0]
        nq = q + move[1]
        if (np > 0) and (nq > 0) and (np < 9) and (nq < 9):
            cnt += 1
    return cnt


# 실행
x,y = currentLocation(location)
answer = moveKnight(x,y)

print(answer)
