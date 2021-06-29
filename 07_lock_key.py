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
    
    idx_key_list = []
    cnt_one = 0
    for i in range(len(key)):
        for j in range(len(key)):
            if lock[i][j] == 1:
                cnt_one += 1
                idx_one = [i,j]
                idx_key_list.append(idx_one)
    if cnt_one == cnt_zero:
        distance_key = calDistance(idx_key_list)
    if distance_key == distance_lock:
        return true
        
        
    
        
    
    answer = True
    return answer