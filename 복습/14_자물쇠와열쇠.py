# p325 자물쇠와 열쇠

def rotate90(li):
    tmp, rotated = [], []
    for i in range(len(li)):
        for j in range(len(li)):
            tmp.append(li[len(li)-j-1][i])
        rotated.append(tmp)
        tmp = []
    return rotated

def openLock(box_li, lock_li):
    lenlock = len(lock_li)
    for i in range(lenlock, lenlock*2):
        for j in range(lenlock, lenlock*2):
            if box_li[i][j] != 1:
                return False
    return True


def solution(key, lock):
    box = []
    for i in range(len(lock)*3):
        box.append([0]*len(lock)*3)
    
    for i in range(len(lock)):
        for j in range(len(lock)):
            box[len(lock) + i][len(lock) + j] = lock[i][j]
    
    for r in range(4):
        key = rotate90(key)
        for bx in range(len(lock)*3):
            for by in range(len(lock)*3):
                for kx in range(len(key)):
                    for ky in range(len(key)):
                        box[bx][by] += key[kx][ky]
                if openLock(box,lock) == True:
                    return True
                for kx in range(len(key)):
                    for ky in range(len(key)):
                        box[bx][by] -= key[kx][ky]
    return False