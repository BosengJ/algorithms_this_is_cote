# p115 왕실의 나이트

position = input("현재 나이트가 위치한 곳의 좌표를 입력하세요:")

row = int(position[1])
column = int(ord(position[0]) - ord('a')) + 1

steps = [
    [-2,1], [-2,-1], # 위
    [2,1], [2,-1],   # 아래
    [1,-2], [-1,-2], # 왼쪽
    [1,2], [-1,2]    # 오른쪽
]

answer = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if (1 <= next_row) and (next_row <= 8) and (1 <= next_column) and (next_column <= 8):
        answer += 1

print(answer)