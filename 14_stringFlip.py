s = input("0과 1로 이뤄진 문자열을 입력하세요")
flip_zero, flip_one = 0,0
for i in range(len(s)):
    if i == len(s)-1:
        if s[i] == '0':
            flip_one += 1
        else:
            flip_zero += 1
    elif (s[i] == '0') and (s[i] != s[i+1]):
        flip_one += 1
    elif (s[i] == '1') and (s[i] != s[i+1]):
        flip_zero += 1

print(flip_one)
print(flip_zero)

if flip_one < flip_zero:
    print(flip_one)
else:
    print(flip_zero)