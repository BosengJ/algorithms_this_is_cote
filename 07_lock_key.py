# key를 90도씩 회전해주는 함수
def rotateKey(li):
    rotated_li = []
    for i in range(len(li)):
        rotated_li.append([0]*len(li))
        
    for i in range(len(li)):
        for j in range(len(li)):
            rotated_li[j][len(li)-i-1] = li[i][j]
    return rotated_li

# 확장된 lock의 가운데 부분이 모두 1인지 확인하는 함수
def checkLock(extended_li,original):
    for i in range(len(original),len(original)*2):
        for j in range(len(original),len(original)*2):
            if extended_li[i][j] != 1:
                return False
    return True

def solution(key, lock):
    # 확장된 Lock array
    extended_lock = []
    for i in range(len(lock)*3):
        extended_lock.append([0]*len(lock)*3)
        
    # 확장된 Lock array 에 기존의 lock array를 가운데에 넣어준다
    for i in range(len(lock)):
        for j in range(len(lock)):
            extended_lock[i+len(lock)][j+len(lock)] = lock[i][j]
    print(extended_lock)
    
    # Sliding Window 
    # 0도 회전한 key를 확장된 lock에 더해주기
    for i in range(len(extended_lock)):
        for j in range(len(extended_lock)):
            extended_lock[i][j] += key[i][j]
        
    
    answer = True
    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
a = solution(key,lock)
print(a)