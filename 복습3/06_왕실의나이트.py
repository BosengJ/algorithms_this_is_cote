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
# input 받은 위치를 행(x)과 열(y)로 수치화해준다
x,y = currentLocation(location)

# 8가지 형태로 중 가능한 이동 횟수를 구해준다
answer = moveKnight(x,y)

print(answer)

'''test case
a1 2
h1 2
a8 2
h8 2
c2 6
b2 4
b7 4
g7 4
g2 4
b4 6
d7 6
g5 6
e2 6
d4 8
c1 4
f1 4
f8 4
c8 4'''