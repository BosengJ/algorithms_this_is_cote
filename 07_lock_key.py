def calDistance(li):
    distance_i = 0
    distance_j = 0
    for i,j in li:
        distance_i -= i
        distance_j -= j
        if distance_i < 0:
            distance_i *= -1
        if distance_j < 0:
            distance_j *= -1
    dx = [distance_i,distance_j]
    return dx

def checkKey(li):
    idx_list = []
    cnt = 0
    for i in range(len(li)):
        for j in range(len(li)):
            if li[i][j] == 1:
                cnt += 1
                idx = [i,j]
                idx_list.append(idx)
    return cnt, idx_list

def solution(key, lock):
    idx_lock_list = []
    cnt_zero = 0
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                cnt_zero += 1
                idx_zero = [i,j]
                idx_lock_list.append(idx_zero)
    distance_lock = calDistance(idx_lock_list)
    print(idx_lock_list)
    print(distance_lock)
    print(cnt_zero)
    
    cnt_one,idx_key_list = checkKey(key)
    if cnt_one == cnt_zero:
        distance_key = calDistance(idx_key_list)
        print(distance_key)
        if distance_key == distance_lock:
            answer = True
        

    answer = True
    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
a = solution(key,lock)
print(a)