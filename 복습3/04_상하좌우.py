# input
# n = int(input("공간의 크기를 나타내는 n을 입력하세요 >"))
# plans = list(input("여행가 A가 이동할 계획서 내용을 공백을 기준으로 입력하세요 >").split())

# test case
n = 5
plans = ['R', 'R', 'R', 'U', 'D', 'D']

# 초기값 세팅
x,y = 1,1

# 방향에 따른 움직임 정보를 가지고 있는 딕셔너리 생성
move_dic = {}
move_dic['L'] = [0,-1]
move_dic['R'] = [0,1]
move_dic['U'] = [-1,0]
move_dic['D'] = [1,0]