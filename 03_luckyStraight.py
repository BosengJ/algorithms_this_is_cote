def solution(N):
    str_N = str(N)
    idx = len(str_N)/2
    back = 0                        # 둘로 나눠진 부분의 앞
    forth = 0                       # 둘로 나눠진 부분의 뒤
    for i in range(len(str_N)):
        if i < idx:
            back += int(str_N[i])
        else:
            forth += int(str_N[i])
    if back == forth:
        return "LUCKY"
    else:
        return "READY"

N = 1000
a = solution(N)
print(a)

'''test case
"123402"
LUCKY

"7755"
READY

"10"
READY

"11"
LUCKY

"99999999"
LUCKY

"99999998"
READY

"1000"
READY
'''