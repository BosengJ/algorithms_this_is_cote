import sys

# n = int(sys.stdin.readline())
# num = list(map(int,sys.stdin.readline().split()))
# add, sub, mul, div = map(int,sys.stdin.readline().split())


n = 2
num = [5,6]
add, sub, mul, div = [0,0,1,0]

def findMax(li):
    M = 0
    for n in li:
        if n > M:
            M = n
    return M

def findMin(li):
    m = li[0]
    for n in li:
        if n < m:
            m = n
    return m
