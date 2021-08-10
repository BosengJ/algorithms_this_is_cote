# p312 곱하기 혹은 더하기

s = input("여러개의 숫자로 구성된 하나의 문자열s를 입력하세요:")

s_li = list(map(int,s))
answer = 0
for num in s_li:
    if answer <= 1:
        answer += num
    elif num <= 1:
        answer += num
    else:
        answer *= num
print(answer)