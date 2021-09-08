# import sys

# n = int(sys.stdin.readline())
# num = list(map(int,sys.stdin.readline().split()))
# add, sub, mul, div = map(int,sys.stdin.readline().split())


n = 2
num = [5,6]
add, sub, mul, div = [0,0,1,0]


def dfs(i, res, add, sub, mul, div):
    global max_, min_
    if i == n:
        if res > max_:
            max_ = res
        if res < min_:
            min_ = res
        return
    else:
        if add:
            dfs(i+1, res+num[i], add-1, sub, mul, div)
        if sub:
            dfs(i+1, res-num[i], add, sub-1, mul, div)
        if mul:
            dfs(i+1, res*num[i], add, sub, mul-1, div)
        if div:
            dfs(i+1, res//num[i], add, sub, mul, div-1)

max_, min_ = -1e9, 1e9
dfs(1,num[0],add,sub,mul,div)

print(max_)
print(min_)