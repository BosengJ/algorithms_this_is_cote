# def checkLock(li):
#     for i in range(len(li))

def solution(key, lock):
    # 확장된 Lock array
    extended_lock = []
    for i in range(len(lock)*3):
        extended_lock.append([0]*len(lock)*3)
        
    # 확장된 Lock array 에 기존의 lock array를 가운데에 넣어준다
    for i in range(len(lock),len(lock)*2):
        for j in range(len(lock),len(lock)*2):
            extended_lock[i][j] += lock[i-len(lock)][j-len(lock)]
    print(extended_lock)
    
    # 0도 회전한 key를 확장된 lock에 더해주기
    # for i in range(len(extended_lock)):
    #     for j in range(len(extended_lock)):
        
    
    answer = True
    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
a = solution(key,lock)
print(a)