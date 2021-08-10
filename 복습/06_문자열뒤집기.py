# p313 문자열 뒤집기

s = input("0과 1로만 이루어진 문자열 s를 입력하세요:")

turntoZero, turntoOne = 0,0
for i in range(len(s)):
    if i == len(s)-1:
        if s[i] == '0':
            turntoOne += 1
        else:
            turntoZero += 1
    elif (s[i] == '0') and (s[i+1] == '1'):
        turntoOne += 1
    elif (s[i] == '1') and (s[i+1] == '0'):
        turntoZero += 1

if turntoZero < turntoOne:
    print(turntoZero)
else:
    print(turntoOne)

# 문자열 뒤집기 test case
# 0001100
# 1

# 10110101
# 3

# 0000000
# 0

# 1111111
# 0

# 1000110001
# 2