def solution(N):
    str_N = str(N)
    idx = len(str_N)/2
    back = 0
    forth = 0
    for i in len(str_N):
        if i < idx:
            back += str_N[i]
        else:
            forth += str_N[i]
    if back = forth:
        return "LUCKY"
    else:
        return "READY"