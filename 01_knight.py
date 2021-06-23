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
    askii_num = int(ord(data_li[0])) - 48
    column = int(chr(askii_num))
    # print(data)
    # print(row,column)

    # 나이트가 위 또는 아래로 2칸 움직일 때
    cnt = 0
    if (row-2 > 0):
        cnt = leftRight(column,cnt)
    if (row+2 < 9):
        cnt = leftRight(column,cnt)

    # 나이트가 왼쪽 또는 오른쪽으로 2칸 움직일 때
    if (column-2 > 0):
        cnt = upDown(row,cnt)
    if (column+2 < 9):
        cnt = upDown(row,cnt)
        
    # print(cnt)
    return cnt

# data = 'a1'
# answer = solution(data)
# print(answer)

data = 'c8'
answer = solution(data)
print(answer)

# a1 2
# h1 2
# a8 2
# h8 2
# c2 6
# b2 4
# b7 4
# g7 4
# g2 4
# b4 6
# d7 6
# g5 6
# e2 6
# d4 8
# c1 4
# f1 4
# f8 4
# c8 4