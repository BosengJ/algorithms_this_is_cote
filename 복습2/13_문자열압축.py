# p323 문자열 압축

def split(u,string):
    li = []
    word = ''
    cnt = 0
    for i in range(len(string)):
        cnt += 1
        word += string[i]
        if u == cnt:
            li.append(word)
            cnt = 0
            word = ''
        elif i == len(string)-1:
            li.append(word)
    return li

def pressure(li):
    cnt = 1
    short = ''
    for i in range(1,len(li)):
        if li[i] != li[i-1]:
            if cnt > 1:
                short += str(cnt)
            short += li[i-1]
            cnt = 0
        if i == len(li)-1:
            cnt += 1
            if cnt > 1:
                short += str(cnt) + li[i]
            else:
                short += li[i]
        else:
            cnt += 1
    return short



def solution(s):
    if len(s) == 1:
        return 1
    
    half = len(s)//2
    short_li = []
    for i in range(1,half+1):
        tmp = split(i,s)
        short_string = pressure(tmp)
        short_li.append(short_string)
    
    min_string = len(short_li[0])
    for s in short_li:
        if len(s) < min_string:
            min_string = len(s)

    return min_string