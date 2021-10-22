# input
n = int(input("공간의 크기를 나타내는 n을 입력하세요 >"))
plans = list(input("여행가 A가 이동할 계획서 내용을 공백을 기준으로 입력하세요 >").split())

# test case
# n = 5

# 초기값 세팅
x,y = 1,1

# 방향에 따른 움직임 정보를 가지고 있는 딕셔너리 생성
move_dic = {}
move_dic['L'] = [0,-1]
move_dic['R'] = [0,1]
move_dic['U'] = [-1,0]
move_dic['D'] = [1,0]

# 주어진 계획서를 가지고 좌표 이동
nx,ny = 0,0
for plan in plans:
    for k,v in move_dic.items():
        if plan == k:
            nx = x + v[0]
            ny = y + v[1]
        if (nx < 1) or (ny < 1) or (nx > n) or (ny > n):
            continue
        x,y = nx,ny
print(x,y)