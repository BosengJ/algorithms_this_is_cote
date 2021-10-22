# input
location = input("현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열을 입력하세요 >")

# 행렬을 수치화 해서 각각의 변수에 저장해주는 함수
def currentLocation(str):
    row = int(str[1])
    column = int(ord(str[0])) - int(ord('a')) + 1
    return row, column

x,y = currentLocation(location)
print(x,y)

