# input
n,m = map(int,input("얼음틀의 세로 길이 n과 가로 길이 m을 공백을 기준으로 입력하세요 >").split())
frame = []
for i in range(n):
    frame.append(list(map(int,input("얼음 틀의 형태를 구멍(0), 그렇지 않은 부분(1)로 입력하세요 >"))))
