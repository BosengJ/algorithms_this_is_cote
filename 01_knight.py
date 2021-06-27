def leftRight(column,cnt):
    if column-1 > 0:
        cnt += 1
    if column+1 < 9:
        cnt += 1
    return cnt

def upDown(row,cnt):
    if row-1 > 0:
        cnt += 1
    if row+1 < 9:
        cnt += 1
    return cnt

def solution(data):
    data_li = list(data)
    row = int(data_li[1])
    
    # column 구하기
    column = int(ord(data_li[0])- ord('a'))
    # column = int(chr(askii_num))

    # 나이트가 위 또는 아래로 2칸 움직일 때
    cnt = 0
    if (row-2 > 0):
        cnt = leftRight(column,cnt) # 왼쪽, 오른쪽으로 1칸 움직일 때
    if (row+2 < 9):
        cnt = leftRight(column,cnt)

    # 나이트가 왼쪽 또는 오른쪽으로 2칸 움직일 때
    if (column-2 > 0):
        cnt = upDown(row,cnt) # 위, 아래로 1칸 움직일 때
    if (column+2 < 9):
        cnt = upDown(row,cnt)
    return cnt

data = 'c8'
answer = solution(data)
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