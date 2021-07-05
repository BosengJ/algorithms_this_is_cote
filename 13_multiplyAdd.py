s_list = list(map(int,input("0부터 9로만 이루어진 문자열을 입력하세요")))

answer = 0
for n in s_list:
    if answer == 0:
        answer += n
    elif n <= 1:
        answer += n
    else:
        answer *= n
print(answer)