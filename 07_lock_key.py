def solution(key, lock):
    idx_lock_list = []
    cnt_zero = 0
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                cnt_zero += 1
                idx_zero = [i,j]
                idx_lock_list.append(idx_zero)
    distance_i = 0
    distance_j = 0
    for i,j in idx_lock_list:
        distance_i -= i
        distance_j -= j
        if distance_i < 0:
            distance_i *= -1
        if distance_j < 0:
            distance_j *= -1
    distance = [distance_i,distance_j]
    print(distance)
    
    answer = True
    return answer