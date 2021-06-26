def splitWord(i,s):
    split_list = []
    word = ""
    for ch in s:
        if len(word) < i:
            word += ch
        else:
            split_list.append(word)
            word = ""
    return split_list

def solution(s):
    half_len_s = len(s)//2
    
    compression_li = []
    for i in range(1,half_len_s+1):
        split_list = splitWord(i,s)
        word = []
        cnt = 0
        for i in range(len(split_list)):
            if i == 0:
                cnt += 1
                word.append(cnt)
                word.append(split_list[i])
            elif s[i] == word[-1]:
                cnt += 1
                word[-2] = cnt
            else:
                cnt = 1
                word.append(cnt)
                word.append(split_list[i])
        compression = ''.join(word)
        compression_li.append(compression)
        print(compression_li)
        
    
    answer = 0
    return answer

s = "aabbaccc"
a = solution(s)
print(a)